import random


def quick_sort_1(arr: list[int]) -> int:
    # Standard QuickSort implementation using the Lomuto partition scheme
    count = 0

    def partition(A, p, r):
        nonlocal count
        x = A[r]  # Choose the last element as the pivot
        i = p - 1

        # Rearrange elements so that those smaller than or equal to pivot are on the left
        for j in range(p, r):
            count += 1
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]

        # Place the pivot in its correct sorted position
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def qs(A, p, r):
        if p < r:
            q = partition(A, p, r)
            # Recursively sort the left and right subarrays
            qs(A, p, q - 1)
            qs(A, q + 1, r)

    if arr:
        qs(arr, 0, len(arr) - 1)

    return count


def randomized_quick_sort(arr: list[int]) -> int:
    # QuickSort with randomized pivot selection to avoid worst-case time complexity
    count = 0

    def partition(A, p, r):
        nonlocal count
        x = A[r]
        i = p - 1
        for j in range(p, r):
            count += 1
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def randomized_partition(A, p, r):
        # Select a random index for the pivot and swap it with the last element
        i = random.randint(p, r)
        A[r], A[i] = A[i], A[r]
        return partition(A, p, r)

    def qs(A, p, r):
        if p < r:
            q = randomized_partition(A, p, r)
            qs(A, p, q - 1)
            qs(A, q + 1, r)

    if arr:
        qs(arr, 0, len(arr) - 1)

    return count


def quick_sort_3_pivot(arr: list[int]) -> int:
    # 3-Pivot QuickSort implementation dividing the array into 4 segments
    count = 0

    def insertion_sort(A, p, r):
        # Fallback sorting algorithm for very small subarrays
        nonlocal count
        for j in range(p + 1, r + 1):
            key = A[j]
            i = j - 1
            while i >= p:
                count += 1
                if A[i] > key:
                    A[i + 1] = A[i]
                    i -= 1
                else:
                    break
            A[i + 1] = key

    def partition_3pivot(A, left, right):
        nonlocal count
        a = left + 2
        b = left + 2
        c = right - 1
        d = right - 1

        # Three pivots required for 4-way partitioning
        p_val = A[left]
        q_val = A[left + 1]
        r_val = A[right]

        # Partitioning loop: group elements into 4 regions based on the 3 pivots
        while b <= c:
            while b <= c:
                count += 1
                if A[b] < q_val:
                    count += 1
                    if A[b] < p_val:
                        A[a], A[b] = A[b], A[a]
                        a += 1
                    b += 1
                else:
                    break

            while b <= c:
                count += 1
                if A[c] > q_val:
                    count += 1
                    if A[c] > r_val:
                        A[c], A[d] = A[d], A[c]
                        d -= 1
                    c -= 1
                else:
                    break

            if b <= c:
                count += 1
                if A[b] > r_val:
                    count += 1
                    if A[c] < p_val:
                        A[b], A[a] = A[a], A[b]
                        A[a], A[c] = A[c], A[a]
                        a += 1
                    else:
                        A[b], A[c] = A[c], A[b]
                    A[c], A[d] = A[d], A[c]
                    b += 1
                    c -= 1
                    d -= 1
                else:
                    count += 1
                    if A[c] < p_val:
                        A[b], A[a] = A[a], A[b]
                        A[a], A[c] = A[c], A[a]
                        a += 1
                    else:
                        A[b], A[c] = A[c], A[b]
                    b += 1
                    c -= 1

        a -= 1
        b -= 1
        c += 1
        d += 1

        # Move the pivots to their final sorted positions
        A[left + 1], A[a] = A[a], A[left + 1]
        A[a], A[b] = A[b], A[a]
        a -= 1

        A[left], A[a] = A[a], A[left]
        A[right], A[d] = A[d], A[right]

        return a, b, d

    def qs(A, p, r):
        n = r - p + 1

        # Use Insertion Sort for subarrays with 3 or fewer elements
        if n <= 3:
            if n > 1:
                insertion_sort(A, p, r)
            return

        # Ensure the 3 pivots are sorted before partitioning
        vals = [A[p], A[p + 1], A[r]]
        vals.sort()
        A[p], A[p + 1], A[r] = vals[0], vals[1], vals[2]

        # Get the final indices of the 3 pivots
        idx1, idx2, idx3 = partition_3pivot(A, p, r)

        # Recursively sort the 4 partitions
        qs(A, p, idx1 - 1)
        qs(A, idx1 + 1, idx2 - 1)
        qs(A, idx2 + 1, idx3 - 1)
        qs(A, idx3 + 1, r)

    if arr:
        qs(arr, 0, len(arr) - 1)

    return count
