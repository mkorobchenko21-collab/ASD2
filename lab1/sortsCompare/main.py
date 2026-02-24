import random
from plotData2 import plot_data
import math


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

    sizes = [10, 100, 1000]
    typesArrayTest = ["random", "randomUniq", "best", "worst"]

    dataPlot = {
        "random": {"bubble": {}, "bubbleImproved": {}, "shell": {}},
        "randomUniq": {"bubble": {}, "bubbleImproved": {}, "shell": {}},
        "best": {"bubble": {}, "bubbleImproved": {}, "shell": {}},
        "worst": {"bubble": {}, "bubbleImproved": {}, "shell": {}},
    }

    for sizeTestArray in sizes:
        print("\nDATA SIZE: ", sizeTestArray)

        for genType in typesArrayTest:
            print("\n\tDATA TYPE:", genType)

            testArray = genArr(sizeTestArray, genType)

            # Bubble sort test
            testArrayBubble = testArray.copy()
            operationCountBubble = bubbleSort(testArrayBubble)
            print("\tBubble sort operation count:", int(operationCountBubble))
            dataPlot[genType]["bubble"][sizeTestArray] = operationCountBubble

            # Bubble sort improved
            testArrayBubbleImproved = testArray.copy()
            operationCountBubbleImproved = bubbleImprovedSort(testArrayBubbleImproved)
            print(
                "\tImproved bubble sort operation count:",
                int(operationCountBubbleImproved),
            )
            dataPlot[genType]["bubbleImproved"][sizeTestArray] = (
                operationCountBubbleImproved
            )

            # Shell sort
            testArrayShell = testArray.copy()
            operationCountShell = shellSort(testArrayShell)
            print("\tShell sort operation count:", int(operationCountShell))
            dataPlot[genType]["shell"][sizeTestArray] = operationCountShell

    plot_data(dataPlot, logarithmic=True, oneplot=True)
