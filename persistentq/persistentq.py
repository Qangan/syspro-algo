import random

class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

class PStack:
    def __init__(self, head=None, size=0):
        self.top = head
        self.size = size

    def push(self, value):
        top = Node(value, self.top)
        return PStack(top, self.size + 1)

    def pop(self):
        return PStack(self.top.prev, self.size - 1), self.top.value

class PQueue:
    def __init__(self, L=PStack(), Ls=PStack(), R=PStack(), Rs=PStack(), S=PStack(), recopy=False, to_copy=0, copied=False):
        self.L = L
        self.Ls = Ls
        self.R = R
        self.Rs = Rs
        self.S = S
        self.recopy = recopy
        self.to_copy = to_copy
        self.copied = copied

    def is_empty(self):
        return not self.recopy and self.R.size == 0

    def push(self, x):
        if not self.recopy:
            Ln = self.L.push(x)
            Qs = PQueue(Ln, self.Ls, self.R, self.Rs, self.S, self.recopy, self.to_copy, self.copied)
            return Qs.checkRecopy()
        else:
            Lns = self.Ls.push(x)
            Qs = PQueue(self.L, Lns, self.R, self.Rs, self.S, self.recopy, self.to_copy, self.copied)
            return Qs.checkNormal()
    
    def pop(self):
        if not self.recopy:
            Rn, x = self.R.pop()
            Qs = PQueue(self.L, self.Ls, Rn, self.Rs, self.S, self.recopy, self.to_copy, self.copied)
            return Qs.checkRecopy(), x
        else:
            Rns, x = self.Rs.pop()
            cur_copy = self.to_copy
            Rn = self.R
            if self.to_copy > 0:
                cur_copy -= 1
            else:
                Rn, _ = Rn.pop()
            Qs = PQueue(self.L, self.Ls, Rn, Rns, self.S, self.recopy, cur_copy, self.copied)
            return Qs.checkNormal(), x
    
    def checkRecopy(self):
        if self.L.size > self.R.size:
            Qs = PQueue(self.L, self.Ls, self.R, self.R, self.S, True, self.R.size, False)
            return Qs.checkNormal()
        else:
            return PQueue(self.L, self.Ls, self.R, self.Rs, self.S, False, self.to_copy, self.copied)

    def checkNormal(self):
        Qs = self.additionalOperations()
        return PQueue(Qs.L, Qs.Ls, Qs.R, Qs.Rs, Qs.S, Qs.S.size > 0, Qs.to_copy, Qs.copied)
    
    def additionalOperations(self):
        to_do = 3
        Rn = self.R
        Sn = self.S
        cur_copied = self.copied

        while (not cur_copied) and to_do > 0 and Rn.size > 0:
            Rn, x = Rn.pop()
            Sn = Sn.push(x)
            to_do -= 1

        Ln = self.L
        while to_do > 0 and Ln.size > 0:
            cur_copied = True
            Ln, x = Ln.pop()
            Rn = Rn.push(x)
            to_do -= 1

        cur_copy = self.to_copy
        while to_do > 0 and Sn.size > 0:
            Sn, x = Sn.pop()
            if cur_copy > 0:
                Rn = Rn.push(x)
                cur_copy -= 1
            to_do -= 1

        Lsn = self.Ls
        if Sn.size == 0:
            Ln, Lsn = Lsn, Ln

        return PQueue(Ln, Lsn, Rn, self.Rs, Sn, self.recopy, cur_copy, cur_copied)

q, xs = PQueue(), []
for _ in range(10000):
    q = q.push(x := random.randint(1, 100000))
    xs.append(x)

for i in xs:
    q, x = q.pop()
    if x != i:
        print("Tests not passed", x, i)
        exit()
print("All tests passed")
