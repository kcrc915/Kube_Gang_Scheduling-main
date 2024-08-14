import pandas
from matplotlib import pyplot as plt
from typing import List

duration_limits: List[int] = [45000, 55000]


def plot_results(file_name: str, title: str) -> None:
    result_df = pandas.read_csv(file_name)
    result_df = result_df.set_index(result_df.columns[0])
    result_df = result_df.drop(columns=result_df.columns[1])
    result_df = result_df.drop(result_df.index[0])
    #print(result_df.head)
    result_df.plot.bar(figsize=(8, 5), ylim=duration_limits)
    plt.xticks(range(0, 20), [str(i) for i in range(1, 21)], rotation=0)
    plt.title(title)
    plt.ylabel('Duration')
    plt.savefig(f"{file_name[:-4]}.png")


def main() -> None:
    plot_results("dyn_mpc.csv","Dynamic MPC results with various window sizes")


if __name__ == "__main__":
    main()