def random_pm(n: int, m: int, a: int, x: int) -> None:
    for i in range(n):
        x = (a * x) % m
        print(x)


random_pm(15, 47, 19, 17)
