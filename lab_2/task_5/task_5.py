def random_awc(n: int, m: int, j: int, k: int, x: list[int]) -> None:
    assert len(x) >= j > k > 0

    l = len(x)
    c = 0

    for i in range(n):
        x1 = x[(i - j) % l]
        x2 = x[(i - k) % l]

        lhs = x1 + x2 + c
        result = lhs % m

        x[i % l] = result
        c = int(lhs >= m)

        print(result)


random_awc(15, 11, 2, 1, [4, 14])
