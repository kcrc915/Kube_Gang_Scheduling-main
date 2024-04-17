import pandas
from matplotlib import pyplot as plt
from typing import List

duration_limits: List[int] = [40000, 70000]


def plot_results(file_name: str, title: str) -> None:
    result_df = pandas.read_csv(file_name)
    result_df = result_df.set_index(result_df.columns[0])
    result_df = result_df.drop(columns=result_df.columns[1])
    result_df.plot.bar(figsize=(8, 13), ylim=duration_limits)
    plt.title(title)
    plt.savefig(f"{file_name[:-4]}.png")


def main() -> None:
    plot_results("C:/Users/k164c194/Desktop/MyProject1/Kube_Gang_Scheduling-main/simulation/Outputs/forecast_results_with_RL.csv",
                 "Simulation Results with forecasts")
    #plot_results("C:/Users/k164c194/Desktop/MyProject1/Kube_Gang_Scheduling-main/simulation/Outputs/forecast _results.csv",
                 #"Simulation Results with Forecasts")

if __name__ == "__main__":
    main()
