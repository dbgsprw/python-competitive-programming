def binary_search(start, end, array, value):
    mid = (start + end) // 2
    if start == end:
        if mid >= len(array) or value == array[mid]:
            return start
        else:
            return start - 1

    if value <= array[mid]:
        return binary_search(start, mid, array, value)
    else:
        return binary_search(mid + 1, end, array, value)


def solution(K, M, A):
    prefix_sum = [A[0]]
    for a in A[1:]:
        prefix_sum.append(prefix_sum[-1] + a)
    min_ = max(A)

    start = 0
    end = len(A)
    for i in range(K - 1):
        previous = prefix_sum[start - 1] if start > 0 else 0
        min_ = max((prefix_sum[-1] - previous) // (K - i), min_)

        idx = binary_search(start, end, prefix_sum, previous + min_)
        start = idx + 1

    previous = prefix_sum[start - 1] if start > 0 else 0
    min_ = max((prefix_sum[-1] - previous), min_)
    return min_

