import numpy as np
from gym import Env
from gym.spaces import Space, Discrete, Box
from stable_baselines3 import DQN
from typing import Dict, List, Tuple, Any
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from simulation.gang_scheduling.resource_configurer import ConfigurationWindow, ResourceConfigurer
from simulation.forecaster.lstm_forecaster import get_actual_dict, get_predictions_dict
from simulation.shared.workloads import WORKLOADS, Workload
from simulation.config.config import (
    SIMULATION_DIR, GANG_SCHEDULING_CHECKPOINT_PENALTY,
    GANG_SCHEDULING_SIMULATION_LENGTH, GANG_SCHEDULING_STARTING_SHARES
)

MODEL_PATH: str = f"{SIMULATION_DIR}/gang_scheduling/models"
A2C_PATH: str = f"{MODEL_PATH}/A2C_MlpPolicy_scaled"
DQN_PATH: str = f"{MODEL_PATH}/DQN_gamma_0.99_lr_0.0005_buffer_100000_exp_frac_0.3"

class SimulatorEnv(Env):
    def __init__(self,
                 resource_configurer: ResourceConfigurer,
                 window_size: int,
                 default_reward: int,
                 default_time_step: int,
                 workloads: List[Workload],
                 actual_workload_sizes: Dict[str, np.ndarray],
                 num_actions: int,
                 duration_low: float,
                 duration_high: float,
                 checkpoint_penalty: int = GANG_SCHEDULING_CHECKPOINT_PENALTY,
                 min_shares: int = GANG_SCHEDULING_STARTING_SHARES,
                 simulation_length: int = GANG_SCHEDULING_SIMULATION_LENGTH):

        self.resource_configurer: ResourceConfigurer = resource_configurer
        self.window_size = window_size
        self.default_reward = default_reward
        self.default_time_step = default_time_step
        self.time_step = self.default_time_step
        self.workloads = workloads
        self.num_actions = num_actions
        self.duration_low = duration_low
        self.duration_high = duration_high
        self.checkpoint_penalty = checkpoint_penalty
        self.min_shares = min_shares
        self.simulation_length = simulation_length
        self.current_config: Dict[str, int] = {
            workload.task.task_name: self.min_shares for workload in self.workloads}
        self.action_space: Space = Discrete(num_actions)
        self.observation_space: Space = Box(low=0, high=1, shape=(
            num_actions, window_size), dtype="float64")
        self.state = self.get_state_from_time_step(self.time_step)
        self.simulation_resource_configurer = ResourceConfigurer(
            workloads=self.workloads,
            predictions=actual_workload_sizes
        )

    def get_durations_from_action(self, time_step: int, action: int) -> np.ndarray:
        durations: np.ndarray = np.empty((self.window_size,))
        if action == 0:
            config = self.current_config
        else:
            config = self.resource_configurer.calculate_resource_configurations(configuration_window=ConfigurationWindow(
                simulation_time_step=time_step, window_size=action
            ))
        for step in range(self.window_size):
            config_window = ConfigurationWindow(
                simulation_time_step=time_step,
                window_size=1,
                starting_prediction=step
            )
            durations[step] = (self.resource_configurer.calculate_estimated_runtime(
                resource_configuration=config,
                configuration_window=config_window
            ) - self.duration_low) * 1.0 / (self.duration_high - self.duration_low)
        return durations

    def get_state_from_time_step(self, time_step: int) -> np.ndarray:
        predicted_durations: List[np.ndarray] = []
        for action in range(self.num_actions):
            action_durations: np.ndarray = self.get_durations_from_action(
                time_step, action)
            predicted_durations.append(action_durations)

        return np.vstack(predicted_durations)

    def step(self, action) -> Tuple[np.ndarray, float, bool, Dict[Any, Any]]:
        # print(action)
        reward = float(self.default_reward)

        next_timestep = ConfigurationWindow(
            simulation_time_step=self.time_step,
            window_size=1
        )

        if action != 0:
            reward -= self.checkpoint_penalty
            configuration_window = ConfigurationWindow(
                simulation_time_step=self.time_step,
                window_size=action
            )
            self.current_config = self.resource_configurer.calculate_resource_configurations(
                configuration_window
            )

        reward -= self.simulation_resource_configurer.calculate_estimated_runtime(
            resource_configuration=self.current_config,
            configuration_window=next_timestep)
        reward = (reward + self.duration_high) / \
            (self.duration_high - self.duration_low)
        self.time_step += 1
        self.state = self.get_state_from_time_step(self.time_step)
        done = self.time_step == self.simulation_length + self.default_time_step
        return self.state, reward, done, {}

    def render(self):
        pass

    def reset(self):
        self.current_config = {
            workload.task.task_name: self.min_shares for workload in self.workloads}
        self.time_step = self.default_time_step
        self.state = self.get_state_from_time_step(self.time_step)
        return self.state


def main():
    predictions: Dict[str, np.ndarray] = get_predictions_dict(WORKLOADS)
    actual: Dict[str, np.ndarray] = get_actual_dict(WORKLOADS)
    resource_configurer: ResourceConfigurer = ResourceConfigurer(
        workloads=WORKLOADS,
        predictions=predictions
    )
    env = SimulatorEnv(
        resource_configurer=resource_configurer,
        window_size=6,
        default_reward=0,
        default_time_step=200,
        workloads=WORKLOADS,
        actual_workload_sizes=actual,
        num_actions=4,
        duration_low=75,
        duration_high=150
    )

    # Define the hyperparameters to tune
    gammas = [0.95, 0.99]  # Discount factor for future rewards
    learning_rates = [1e-3, 5e-4]  # Learning rate for the optimizer
    buffer_sizes = [50000, 100000]  # Maximum number of transitions stored in the replay buffer
    exploration_fractions = [0.1, 0.3]  # Fraction of training duration for exploration annealing

    # Train multiple models with different hyperparameters
    for gamma in gammas:
        for learning_rate in learning_rates:
            for buffer_size in buffer_sizes:
                for exploration_fraction in exploration_fractions:
                    model = DQN("MlpPolicy", env, verbose=2, gamma=gamma, learning_rate=learning_rate, buffer_size=buffer_size, exploration_fraction=exploration_fraction)
                    model.learn(total_timesteps=10000, log_interval=1)
                    model_name = f"DQN_gamma_{gamma}_lr_{learning_rate}_buffer_{buffer_size}_exp_frac_{exploration_fraction}.zip"
                    model.save(MODEL_PATH + '/' + model_name)
                    print(f"Model Saved: {model_name}")


if __name__ == "__main__":
    main()
