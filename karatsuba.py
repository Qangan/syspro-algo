import random


def karatsuba(n: int, m: int) -> int:
    if n < 10 and m < 10:
        return n * m

    maxlen = max(len(str(n)), len(str(m)))
    pivot = maxlen // 2

    xl = n // (10 ** pivot)
    xr = n % (10 ** pivot)

    yl = m // (10 ** pivot)
    yr = m % (10 ** pivot)

    a = karatsuba(xl, yl)
    d = karatsuba(xr, yr)
    e = karatsuba((xl + xr), (yl + yr)) - a - d

    return a * (10 ** (pivot * 2)) + e * (10 ** pivot) + d


for i in range(1000):
    a, b = [random.randint(1, 10**9) for j in range(2)]
    if karatsuba(a, b) != a * b:
        print("Test failed", a, b, a*b, karatsuba(a, b))
        exit(0)
print("All tests passed!")
