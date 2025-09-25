class Task:
    def __init__(self, deadline: int, penalty: int):
        self.deadline = deadline
        self.penalty = penalty
        self.time = None
    
    def __repr__(self):
        return f"dd: {self.deadline} pen: {self.penalty}"

class UF:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.low = list(range(n + 1))
        self.high = list(range(n + 1))

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.low[x] = min(self.low[x], self.low[y])
        self.high[x] = max(self.high[x], self.high[y])
        return x

def naive_schedule(tasks):
    n = max(map(lambda x: x.deadline, tasks))
    tasks.sort(key=lambda t: t.penalty, reverse=True)
    D = [0] * (n + 1)

    for task in tasks:
        for t in range(task.deadline):
            if D[t] == 0:
                D[t] = task
                task.time = t
                break
        else:
            task.time = None
    ans = 0
    for task in tasks:
        if task.time is None:
            ans += task.penalty
    return ans

def schedule_tasks(tasks):
    n = max(map(lambda x: x.deadline, tasks)) 
    tasks.sort(key=lambda x: x.penalty, reverse=True)
    D = [0] * (n + 1)
    uf = UF(n + 1)

    for task in tasks:
        time = task.deadline
        if time >= 1 and D[time] != 0:
            root = uf.find(D[time])
            time = uf.low[root] - 1
        if time < 1:
            task.time = None
            continue
        task.time = time
        D[time] = time
        if time - 1 >= 1 and D[time - 1] != 0:
            uf.union(D[time - 1], D[time])
        if time + 1 <= n and D[time + 1] != 0:
            uf.union(D[time], D[time + 1])
    ans = 0
    for task in tasks:
        if task.time is None:
            ans += task.penalty
    return ans
