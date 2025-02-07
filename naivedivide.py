import random


def naive_divide(n: int, m: int) -> tuple[int, int]:
    p, r = 0, 0
    str_n = str(n)
    for i in range(len(str_n)): 
        r = r * 10 + int(str_n[i])
        ans_part = 0
        while r >= m: 
            r -= m
            ans_part += 1
        p = p * 10 + ans_part
    return p, r


for i in range(1000):
    n, m = [random.randint(1, 10**5) for i in range(2)]
    if naive_divide(n, m) != (n//m, n % m):
        print("TEST FAILED", n, m)
        exit(0)
print("All tests passed!")
