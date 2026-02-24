import random
import classes
import math
# from plotData import plot_data


def genArr(size: int, genType: str = "random") -> list:
    match genType:
        case "best":
            return [i for i in range(1, size + 1)]
        case "worst":
            return [i for i in reversed(range(1, size + 1))]
        case "random":
            return [random.randint(1, size) for _ in range(1, size + 1)]
        case "randomUniq":
            arr = [i for i in range(1, size + 1)]
            random.shuffle(arr)
            return arr


def print_result(results: list["classes.SortResult"]):
    old_size = None
    old_algo = None
    for r in results:
        current_size = r.size
        if current_size != old_size:
            print(f"Size: {current_size}")

        current_algo = r.algorithm
        if current_algo != old_algo:
            print(f"\t{r.algorithm} sort:")

        print(f"\t\tType: {r.data_type:<10}\t{r.operations:>10,}")

        old_size = current_size
        old_algo = current_algo


def bubbleSort(arr: list) -> int:
    size = len(arr)
    operationCount = 0

    for i in range(size - 1):
        for j in range(size - i - 1):
            operationCount += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return operationCount


def bubbleImprovedSort(arr: list) -> int:
    size = len(arr)
    operationCount = 0

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            operationCount += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return operationCount


def shellSort(arr: list) -> int:  # using Tokuda gap
    def getTokudaGaps(n: int) -> list:
        gaps = []
        k = 1
        while (
            gap := math.ceil((9**k - 4**k) / (5 * 4 ** (k - 1)))
        ) <= n:  # while this new counted gap <= n
            gaps.append(gap)
            k += 1

        return reversed(gaps)

    size = len(arr)
    operationCount = 0
    gaps = getTokudaGaps(size)

    for gap in gaps:
        for i in range(gap, size):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                operationCount += 1
                arr[j] = arr[j - gap]
                j -= gap

            if j >= gap:  # when in while loop was comparison, but it didnt counted
                operationCount += 1

            arr[j] = temp

    return operationCount


if __name__ == "__main__":
    #
    # TESTS
    #

    algorithms = [
        classes.SortAlgorithm(name="bubble", func=bubbleSort),
        classes.SortAlgorithm(name="bubbleImproved", func=bubbleImprovedSort),
        classes.SortAlgorithm(name="shell", func=shellSort),
    ]

    Experiment = classes.SortExperiment(
        sizes=[10, 100, 1000],
        data_types=["random", "randomUniq", "best", "worst"],
        algorithms=algorithms,
    )

    Experiment.run()

    algo_order = {
        "bubble": 0,
        "bubbleImproved": 1,
        "shell": 2,
    }

    sorted_results = sorted(
        Experiment.results, key=lambda r: (r.size, algo_order[r.algorithm])
    )

    print_result(sorted_results)

    # plot_data(experiment.results)
    # plot_data(dataPlot, logarithmic=True, oneplot=True)
