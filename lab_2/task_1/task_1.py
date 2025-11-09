def gcd_unoptimized(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd_optimized(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


def lcm(a: int, b: int) -> int:
    ab_product = a * b

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return ab_product // a


print(gcd_unoptimized(6, 9))
print(gcd_optimized(6, 9))
print(lcm(6, 9))
