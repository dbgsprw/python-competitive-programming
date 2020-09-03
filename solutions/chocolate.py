def gcd(big, small):
    if small == 0:
        return big
    return gcd(small, big % small)


def solution(N, M):
    return int(N / gcd(N, M))

