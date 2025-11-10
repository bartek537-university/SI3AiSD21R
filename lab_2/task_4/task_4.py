def random_lcg(n: int, m: int, a: int, c: int, x: int) -> None:
    for i in range(n):
        x = (a * x + c) % m
        print(x)


random_lcg(15, 47, 28, 8, 17)
