import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def vm_stats(df: pd.DataFrame):
    iteration_count = df.drop(columns=['Count']).groupby('DestinationVmName').max('Iteration')
    avg_hits_per_iteration = df.drop(columns=['Iteration']).groupby('DestinationVmName').mean()

    return {'iteration_count': iteration_count, 'avg_hits_per_iteration': avg_hits_per_iteration}


def plot(stat_before, stat_after, column, ylabel, title):
    # X and same appear to match each other
    X = stat_before.index.tolist()
    # same = load_after.index.tolist()

    # use shorter names on plot's X axis
    x = list(map(lambda vm_name: vm_name[:15], X))

    y_before = stat_before[column].tolist()
    y_after = stat_after[column].tolist()

    x_axis = np.arange(len(x))
    plt.bar(x_axis - 0.2, y_before, 0.4, label='Before')
    plt.bar(x_axis + 0.2, y_after, 0.4, label='After')

    plt.xticks(x_axis, x)
    plt.xlabel("DestinationVmName")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def main(before: pd.DataFrame, after: pd.DataFrame):
    stats_before = vm_stats(before)
    stats_after = vm_stats(after)

    plot(
        stats_before['avg_hits_per_iteration'],
        stats_after['avg_hits_per_iteration'],
        column="Count",
        ylabel="Hits",
        title="Average iteration VM load"
    )
    plot(
        stats_before['iteration_count'],
        stats_after['iteration_count'],
        column="Iteration",
        ylabel="Iterations",
        title="Iterations a VM went through"
    )


def check_args():
    if len(sys.argv[1:]) != 2:
        print(f"Missing arguments. Usage: python {sys.argv[0]} LOAD_BEFORE_CSV_PATH LOAD_AFTER_CSV_PATH")
        sys.exit()


if __name__ == "__main__":
    check_args()
    before_path = sys.argv[1]
    after_path = sys.argv[2]

    df_before = pd.read_csv(before_path)
    df_after = pd.read_csv(after_path)

    main(df_before, df_after)
