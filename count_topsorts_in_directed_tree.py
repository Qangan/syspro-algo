from math import factorial
from itertools import permutations
import random


def comb_count(tree: list[list[int]]):
    n = len(tree)
    sz = [0] * n

    def dfs(i):
        sz[i] = 1
        for j in tree[i]:
            dfs(j)
            sz[i] += sz[j]

    dfs(0)

    fact = factorial(n)
    k = 1
    for i in range(n):
        k *= sz[i]

    return fact // k

def brute_force(tree: list[list[int]]):
    ans = 0
    edges = [(i,j) for i in range(len(tree)) for j in tree[i]]
    
    for i in permutations(range(len(tree))):
        if all(i[x] < i[y] for x, y in edges):
            ans += 1

    return ans

tests = []
tests.append([[]])
tests.append([[1], [2], [3], []]) 
tests.append([[1,2,3], [], [], []])
tests.append([[1,2], [3,4], [5,6], [], [], [], []])
tests.append([[1,3,4], [2], [], [], []])
tests.append([[1,2], [], [3], [4], []])
tests.append([[1,2], [], [3,4], [], []])
tests.append([[1,2], [3], [4], [], []])
tests.append([[1], [2,3], [4], [], []])

for i in range(10):
    tree = [[] for j in range(10)]
    for k in range(1, 10):
        tree[random.randint(0, k-1)].append(k)
    tests.append(tree)

for _, tree in enumerate(tests):
    print(tree)
    brute = brute_force(tree)
    ans = comb_count(tree)
    assert ans == brute, f"{brute} {ans}"
print("All tests passed")
