def solution(A):
    destination = len(A)

    fibonacci_list = [0, 1]
    while -1 + fibonacci_list[-1] < destination:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    fibonacci_set = set(fibonacci_list)

    leaves_indexes = [-1] + [i for i in range(0, destination) if A[i] == 1] + [destination]
    min_cnt = [0] + [-1] * (len(leaves_indexes) - 1)

    for i in range(1, len(leaves_indexes)):
        for j in range(0, i):
            distance = leaves_indexes[i] - leaves_indexes[j]
            if distance in fibonacci_set and min_cnt[j] != -1:
                if min_cnt[i] == -1 or min_cnt[j] + 1 < min_cnt[i]:
                    min_cnt[i] = min_cnt[j] + 1

    return min_cnt[-1]
