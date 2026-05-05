import random


def quick_sort_1(arr: list[int]) -> int:
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

    def qs(A, p, r):
        if p < r:
            q = partition(A, p, r)
            qs(A, p, q - 1)
            qs(A, q + 1, r)

    if arr:
        qs(arr, 0, len(arr) - 1)

    return count


def randomized_quick_sort(arr: list[int]) -> int:
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
        # Випадковий вибір опорного елементу
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
    """
    Алгоритм 3. Швидке сортування з 3 опорними елементами.
    """
    count = 0

    def insertion_sort(A, p, r):
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
        p_val = A[left]
        q_val = A[left + 1]
        r_val = A[right]

        while b <= c:
            # Розбиваємо while на умову та break, щоб правильно рахувати порівняння
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

        A[left + 1], A[a] = A[a], A[left + 1]
        A[a], A[b] = A[b], A[a]
        a -= 1

        A[left], A[a] = A[a], A[left]
        A[right], A[d] = A[d], A[right]

        return a, b, d

    def qs(A, p, r):
        n = r - p + 1
        if n <= 3:
            if n > 1:
                insertion_sort(A, p, r)
            return

        # Впорядковуємо 3 опорні елементи: A[p], A[p+1], A[r]
        # За вимогами методички, порівняння тут НЕ йдуть у загальний лічильник!
        vals = [A[p], A[p + 1], A[r]]
        vals.sort()
        A[p], A[p + 1], A[r] = vals, vals[1], vals[2]

        idx1, idx2, idx3 = partition_3pivot(A, p, r)

        qs(A, p, idx1 - 1)
        qs(A, idx1 + 1, idx2 - 1)
        qs(A, idx2 + 1, idx3 - 1)
        qs(A, idx3 + 1, r)

    if arr:
        qs(arr, 0, len(arr) - 1)

    return count
