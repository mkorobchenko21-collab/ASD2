import numpy as np
import random
from plot_data import plot_data
import math


def genArr(size, genType = "random"):
    if genType == "best":
        a = [i for i in range(1, size)]
    elif genType == "worst":
        a = [i for i in reversed(range(1, size))]
    else:
        a = [random.randint(1, size) for _ in range(1, size)]

    return a

def bubbleSort(arr):
    size = len(arr)
    operationCount = 0
 
    for i in range(size - 1):
        for j in range(size - i - 1):
            operationCount += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return operationCount


def bubbleImprovedSort(arr):
    size = len(arr)
    operationCount = 0

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            operationCount += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

    return operationCount


def shellSort(arr): # using Tokuda gap
    def getTokudaGaps(n):
            gaps = []
            k = 1
            while (gap := math.ceil((9**k - 4**k) / (5 * 4**(k - 1))) ) <= n:       # while this new counted gap <= n
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

            if j >= gap: # when in while loop was comparison, but it didnt counted
                operationCount += 1

            arr[j] = temp

    return operationCount

if __name__ == "__main__":
    """
    ТЕСТУВАННЯ АЛГОРИТМІВ:
    тестування проводиться на наборах розімром 10, 100, 1000, 10000 (масив sizes)
    але для початкової перевірки роботи рекомендується використовувати тільки
    перші дві-три величини
    """

    sizes = [10, 100, 1000]
    types = ["random", "best", "worst"]

    data_plot = {
        'random': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
        'best': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
        'worst': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}}
    }

    for n in sizes:
        print ("\nDATA SIZE: ", n)

        for gen_type in types:
            print ("\n\tDATA TYPE:", gen_type)

            data = genArr(n, gen_type)

            data_bubble = np.copy(data)
            bubble_op_count = bubbleSort(data_bubble)
            print ("\tBubble sort operation count:", int(bubble_op_count))
            data_plot[gen_type]['bubble'][n] = bubble_op_count

            # Для тестування покращеного методу бульбашки
            data_bubble_impr = np.copy(data)
            bubble_impr_op_count = bubbleImprovedSort(data_bubble_impr)
            print ("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
            data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count

            data_insertion = np.copy(data)
            #insertion_op_count = insertion_sort(data_insertion)
            # print ("\tInsertion sort operation count:", int(insertion_op_count))
            # data_plot[gen_type]['insertion'][n] = insertion_op_count

# plot_data(data_plot, logarithmic=True, oneplot=True)
