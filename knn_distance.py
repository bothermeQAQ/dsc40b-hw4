def knn_distance(arr, q, k):
    A = [(abs(x - q), x) for x in arr]
    target = k - 1

    def partition(lo, hi):
        pivot = A[hi][0]
        i = lo
        for j in range(lo, hi):
            if A[j][0] <= pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[hi] = A[hi], A[i]
        return i

    def quickselect(lo, hi, idx):
        while lo <= hi:
            p = partition(lo, hi)
            if p == idx:
                return
            if p < idx:
                lo = p + 1
            else:
                hi = p - 1

    quickselect(0, len(A) - 1, target)
    d, x = A[target]
    return d, x
