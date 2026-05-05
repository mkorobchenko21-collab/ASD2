import random
import classes
import math
from plotData import DataPlotter


def gen_arr(size: int, gen_type: str = "random") -> list:
    # to generate an array for testing sorting algorithms
    match gen_type:
        case "best":
            return [i for i in range(1, size + 1)]
        case "worst":
            return [i for i in reversed(range(1, size + 1))]
        case "random":
            arr = [i for i in range(1, size + 1)]
            random.shuffle(arr)
            return arr


def sort_result(arr: list["classes.SortExperiment"]):
    algo_order = {
        "bubble": 0,
        "bubbleImproved": 1,
        "shell": 2,
    }

    return sorted(arr, key=lambda r: (r.size, algo_order[r.algorithm]))


def print_result(results: list["classes.SortResult"]):
    """
    Prints formatted sorting statistics grouped by input size and algorithm.

    The function expects a list of SortResult objects sorted by:
    1) size
    2) algorithm

    example of print:
        Size: 10
            bubble sort:
                    Type: random                    45
                    Type: best                      45
                    Type: worst                     45
            bubbleImproved sort:
                    Type: random                    44
                    ...
    """

    old_size = None
    old_algo = None
    for obj in results:
        current_size = obj.size
        if current_size != old_size:
            print(f"Size: {current_size}")

        current_algo = obj.algorithm
        if current_algo != old_algo:
            print(f"\t{obj.algorithm} sort:")

        print(f"\t\tType: {obj.data_type:<10}\t{obj.operations:>10,}")

        old_size = current_size
        old_algo = current_algo


def bubble_sort(arr: list) -> int:
    size = len(arr)
    operation_count = 0

    for i in range(size - 1):
        for j in range(size - i - 1):
            operation_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return operation_count


def bubble_improved_sort(arr: list) -> int:
    size = len(arr)
    operation_count = 0

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            operation_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return operation_count


def shell_sort(arr: list) -> int:  # using Tokuda gap
    def get_tokuda_geps(n: int) -> list:
        gaps = []
        k = 1
        # while this new counted gap <= n
        while (gap := math.ceil((9**k - 4**k) / (5 * 4 ** (k - 1)))) <= n:
            gaps.append(gap)
            k += 1

        return reversed(gaps)

    size = len(arr)
    operation_count = 0
    gaps = get_tokuda_geps(size)

    for gap in gaps:
        for i in range(gap, size):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                operation_count += 1
                arr[j] = arr[j - gap]
                j -= gap

            if j >= gap:  # when in while loop was comparison, but it didnt counted
                operation_count += 1

            arr[j] = temp

    return operation_count


if __name__ == "__main__":
    #
    # TESTS
    #

    algorithms = [
        classes.SortAlgorithm(name="bubble", func=bubble_sort),
        classes.SortAlgorithm(name="bubbleImproved", func=bubble_improved_sort),
        classes.SortAlgorithm(name="shell", func=shell_sort),
    ]

    Experiment = classes.SortExperiment(
        sizes=[10, 100, 1000, 2000, 3000, 4000, 5000],
        data_types=["random", "best", "worst"],
        algorithms=algorithms,
    )

    Experiment.run()

    sorted_results = sort_result(Experiment.results)

    print_result(sorted_results)

    plotter = DataPlotter(Experiment.results)
    plotter.plot(logarithmic=True, one_plot=False)
