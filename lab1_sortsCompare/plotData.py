import matplotlib.pyplot as plt
from collections import defaultdict

from math import log10


class DataPlotter:
    def __init__(self, results: list["SortResult"]):

        self.results = results

    def _group(self):
        """

        data[data_type][algorithm][size] = operations

        """

        data = defaultdict(lambda: defaultdict(dict))

        for r in self.results:
            data[r.data_type][r.algorithm][r.size] = r.operations

        return data

    def plot(self, logarithmic: bool = False, one_plot: bool = False):

        grouped = self._group()

        num_plots = 1 if one_plot else len(grouped)

        fig, axes = plt.subplots(num_plots, 1, figsize=(8, 5 * num_plots))

        if num_plots == 1:
            axes = [axes]

        for ax, (data_type, algos) in zip(axes, grouped.items()):
            for algo, points in algos.items():
                sizes = sorted(points.keys())

                ops = [points[s] for s in sizes]

                if logarithmic:
                    sizes = [log10(x) for x in sizes]

                    ops = [log10(y) for y in ops]

                ax.plot(sizes, ops, marker="o", label=algo)

            ax.set_title(f"Data type: {data_type}")

            ax.set_xlabel("Size")

            ax.set_ylabel("Operations")

            ax.grid(True)

            ax.legend()

        plt.tight_layout()

        plt.show()
