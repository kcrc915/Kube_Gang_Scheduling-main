import pandas
import seaborn
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List

from simulation.config.config import SIMULATION_DIR, PROFILER_OUTPUT_PATH
from simulation.shared.workloads import Workload, WORKLOADS


def generate_workload_figures(workloads: List[Workload]):
    df = pandas.read_csv(SIMULATION_DIR + PROFILER_OUTPUT_PATH)

    output_dir = Path(SIMULATION_DIR) / "workload_profiler" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.rcParams.update({
        "font.size": 18,
        "axes.labelsize": 16,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "pdf.fonttype": 42,
    })

    for workload in workloads:
        task_name = workload.task.task_name

        workload_df = df[df[df.columns[0]] == task_name][df.columns[1:]]
        workload_df = workload_df.pivot(
            index=workload_df.columns[0],
            columns=workload_df.columns[1],
            values=workload_df.columns[2],
        )

        fig, ax = plt.subplots(figsize=(8, 8))

        seaborn.heatmap(
            workload_df,
            ax=ax,
            xticklabels=True,
            yticklabels=True,
            rasterized=False,
        )

        # Keep both the heatmap and color bar as vector graphics.
        for figure_ax in fig.axes:
            for collection in figure_ax.collections:
                collection.set_rasterized(False)

        ax.set_title(f"Workload Profiling - {task_name}")
        ax.set_xlabel("CPU Shares")
        ax.set_ylabel("Workload Size")
        ax.tick_params(axis="x", labelrotation=90)
        ax.tick_params(axis="y", labelrotation=90)

        fig.savefig(output_dir / f"{task_name}.pdf")
        plt.close(fig)


def main():
    generate_workload_figures(WORKLOADS)


if __name__ == "__main__":
    main()