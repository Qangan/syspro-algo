import numpy as np
from numbers import Number
from numpy.typing import *
from time import time
import random

def naive_mult(a: NDArray[NDArray[int]], b: NDArray[NDArray[int]]) -> NDArray[NDArray[int]]:
    c = np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i, j] += a[i, k] * b[k, j]
    return c

def simple_mul(x: NDArray[NDArray[int]], y: NDArray[NDArray[int]]) -> NDArray[NDArray[int]]:
    n = len(x)
    
    if n <= 2:
        return np.dot(x, y)
    
    pivot = n // 2
    a = x[:pivot, :pivot]
    b = x[:pivot, pivot:]
    c = x[pivot:, :pivot]
    d = x[pivot:, pivot:]
    e = y[:pivot, :pivot]
    f = y[:pivot, pivot:]
    g = y[pivot:, :pivot]
    h = y[pivot:, pivot:]
    
    ae = simple_mul(a, e)
    bg = simple_mul(b, g)
    af = simple_mul(a, f)
    bh = simple_mul(b, h)
    ce = simple_mul(c, e)
    dg = simple_mul(d, g)
    cf = simple_mul(c, f)
    dh = simple_mul(d, h)

    q1 = ae + bg
    q2 = af + bh
    q3 = ce + dg
    q4 = cf + dh

    return np.vstack((np.hstack((q1, q2)), np.hstack((q3, q4))))

def strassen(x: NDArray[NDArray[int]], y: NDArray[NDArray[int]]) -> NDArray[NDArray[int]]:
    n = len(x)
    
    if n <= 2:
        return np.dot(x, y)
    
    pivot = n // 2
    a = x[:pivot, :pivot]
    b = x[:pivot, pivot:]
    c = x[pivot:, :pivot]
    d = x[pivot:, pivot:]
    e = y[:pivot, :pivot]
    f = y[:pivot, pivot:]
    g = y[pivot:, :pivot]
    h = y[pivot:, pivot:]
    
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)
    
    q1 = p5 + p4 - p2 + p6
    q2 = p1 + p2
    q3 = p3 + p4
    q4 = p5 + p1 - p3 - p7   
    return np.vstack((np.hstack((q1, q2)), np.hstack((q3, q4))))

def format_table(benchmarks: list[str], algos: list[str], results: list[list[Number]]) -> None:
    mcl = max(len(case) for case in benchmarks)
    mtl = max(len(tp) for tp in algos)
    mrl = max(len(str(i)) for j in results for i in j)

    cell = max(mcl, mtl, mrl, 10)

    head = f"| {'yenchmark':<{cell}} | " + " | ".join(f"{tp:<{cell}}" for tp in algos) + " |"
    
    top =  "┏" + '-' * (len(head) - 2) + '┒'
    sep =  '|' + '-' * (len(head) - 2) + '|'
    bot = '┖' + '-' * (len(head) - 2) + '┛'
    
    print(top)
    print(head)
    print(sep)

    for case, rest in zip(benchmarks, results):
        row = f"| {case:<{cell}} | " + \
              ' | '.join(f"{val:<{cell}}" for val in rest) + " |"
        print(row)
    
    print(bot)

benches = [str(2**i) for i in range(11)]
algos = ["Naive", "Naive D&C", "Shtrassen"]
times = [[] for i in range(11)]

for i in range(11):
    print(i)
    a = np.random.randint(1, 10**6, size=(2**i, 2**i))
    b = np.random.randint(1, 10**6, size=(2**i, 2**i))
    
    t1 = time()
    r1 = naive_mult(a,b)
    t2 = time()
    times[i].append(t2 - t1)

    t1 = time()
    r2 = simple_mul(a,b)
    t2 = time()
    times[i].append(t2 - t1)

    t1 = time()
    r3 = strassen(a,b)
    t2 = time()
    times[i].append(t2 - t1)

    if not np.array_equal(r1, r2) or not np.array_equal(r1, r3):
        print("Test not passed", r1, r2, r3, a, b)
format_table(benches, algos, times)

