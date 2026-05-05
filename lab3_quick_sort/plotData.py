import matplotlib.pyplot as plt
from math import log10


def plot_sort_results(
    data_dict: dict, logarithmic: bool = False, one_plot: bool = False
) -> None:

    num_plots = 1 if one_plot else len(data_dict)

    fig, axes = plt.subplots(num_plots, 1, figsize=(8, 5 * num_plots))

    if num_plots == 1:
        axes = [axes]

    for ax, (data_type, algos) in zip(axes, data_dict.items()):
        for algo, points in algos.items():
            sizes = sorted(points.keys())
            ops = [points[s] for s in sizes]

            if logarithmic:
                sizes = [log10(x) for x in sizes]
                ops = [log10(y) for y in ops]

            ax.plot(sizes, ops, marker="o", label=algo)

        ax.set_title(f"Data type: {data_type}")

        ax.set_xlabel("Log10(Size)" if logarithmic else "Size")
        ax.set_ylabel("Log10(Operations)" if logarithmic else "Operations")

        ax.grid(True, linestyle="--", alpha=0.7)
        ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sample_data = {
        "Random Array": {
            "QuickSort 1": {10: 30, 100: 450, 1000: 5000},
            "QuickSort 2": {10: 25, 100: 400, 1000: 4800},
        },
        "Reversed Array": {
            "QuickSort 1": {10: 45, 100: 5000, 1000: 500000},
            "QuickSort 2": {10: 20, 100: 390, 1000: 4700},
        },
    }

    plot_sort_results(sample_data, logarithmic=False, one_plot=False)
