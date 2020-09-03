def solution(A, B):
    calculated_binary = [1, 2]
    for i in range(2, max(B) + 1):
        calculated_binary.append(calculated_binary[-1] * 2)

    fibonacci = [1, 1]
    for i in range(2, max(A) + 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    result = []
    cache = {}
    for a, b in zip(A, B):
        if (a, b) in cache:
            result.append(cache[(a, b)])
        else:
            cache[(a, b)] = fibonacci[a] % calculated_binary[b]
            result.append(cache[(a, b)])
    return result
