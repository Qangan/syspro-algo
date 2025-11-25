import random

class Node:
    def __init__(self, l, r, a):
        self.l = l
        self.r = r
        self.a = a

class PST:
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr
        self.sarr = sorted(arr)
        self.roots = [self.build(0, self.N - 1)]
        for i in sorted([i for i in range(self.N)], key =lambda x: self.arr[x], reverse=True):
            self.roots.append(self.revive(self.roots[-1], 0, self.N - 1, i))

    def build(self, l, r):
        if l == r:
            return Node(None, None, 0)
        m = (l+r)//2 
        l, r = self.build(l, m), self.build(m + 1,r)
        return Node(l, r, l.a + r.a)
    
    def revive(self, root, l, r, idx):
        if l == r:
            return Node(None, None, True)
        m = (l + r) // 2
        rl, rr = (self.revive(root.l, l, m, idx), root.r) if idx <= m else (root.l, self.revive(root.r, m+1, r, idx))
        return Node(rl, rr, rl.a + rr.a)

    def _gte(self, root, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return root.a
        m = (tl + tr) // 2
        return (self._gte(root.l, tl, m, l, min(r, m)) if l <= m else 0) + (self._gte(root.r, m + 1, tr, max(l, m + 1), r) if r > m else 0)

    def binsearch(self, x: int):
        l, h = 0, len(self.sarr)
        while l < h:
            m = (l + h) // 2
            if self.sarr[m] < x:
                l = m + 1
            else:
                h = m
        return l

    def gte(self, l, r, k):
        gen = self.N - self.binsearch(k)
        return self._gte(self.roots[gen], 0, self.N - 1, l, r) 

for i in range(1000):
    n = random.randint(1, 1000)
    arr, k = [random.randint(0, 10000) for i in range(n)], random.randint(0, 10000)
    pst = PST(arr)
    r = random.randint(l := random.randint(0, n - 1), n - 1)
    if (pst.gte(l, r, k) != sum([1 for i in arr[l:r+1] if i >= k])):
        print(pst.gte(l, r, k), sum([1 for i in arr[l:r+1] if i >= k]))
        print(arr)
        exit()
print("ALL TESTS PASSED")
