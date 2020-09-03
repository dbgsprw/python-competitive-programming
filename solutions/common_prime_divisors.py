def solution(A, B):
    result = 0
    for a, b in zip(A, B):
        gcd = get_gcd(*sorted([a, b]))
        result += 1 if check(a, gcd) and check(b, gcd) else 0

    return result


def get_gcd(big, small):
    if small == 0:
        return big
    return get_gcd(small, big % small)


def check(number, gcd):
    gcd_of_gcd = get_gcd(*sorted([number, gcd]))
    if number / gcd_of_gcd == 1:
        return True
    if gcd_of_gcd == 1:
        return False

    return check(number / gcd_of_gcd, gcd)
