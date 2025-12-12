from collections import deque
import random


class Node:

    def __init__(self, parent=None, fromParent=None) -> None:
        self.terminal = False
        self.go = {}
        self.suffLink = None
        self.parent = parent
        self.fromParent = fromParent
        self.count = 0
        self.pattern = None


class Trie:

    def __init__(self) -> None:
        self.root = Node()
        self.root.suffLink = self.root
        self.bfs = []
        self.patterns = []

    def add_pattern(self, pattern: str) -> None:
        self.bfs = []
        self.patterns.append(pattern)
        v = self.root
        for c in pattern:
            if c not in v.go:
                v.go[c] = Node(parent=v, fromParent=c)
            v = v.go[c]
        v.terminal = True
        v.pattern = pattern

    def build(self) -> None:
        queue = deque()
        self.bfs = []
        for c, child in self.root.go.items():
            child.suffLink = self.root
            queue.append(child)
            self.bfs.append(child)
        while queue:
            v = queue.popleft()
            for c, child in v.go.items():
                temp = v.suffLink
                while temp != self.root and c not in temp.go:
                    temp = temp.suffLink
                if c in temp.go:
                    child.suffLink = temp.go[c]
                else:
                    child.suffLink = self.root
                queue.append(child)
                self.bfs.append(child)

    def search(self, text: str) -> tuple[dict[str, list[int]], dict[str, int]]:
        if not self.bfs:
            self.build()
        self.root.count = 0
        for node in self.bfs:
            node.count = 0
        pos = {p: [] for p in self.patterns}
        v = self.root
        for i, c in enumerate(text):
            while v != self.root and c not in v.go:
                v = v.suffLink
            if c in v.go:
                v = v.go[c]
            v.count += 1
            temp = v
            while temp != self.root:
                if temp.terminal:
                    pos[temp.pattern].append(i - len(temp.pattern) + 1)
                temp = temp.suffLink
        for node in reversed(self.bfs):
            node.suffLink.count += node.count
        counts = {}
        for pattern in self.patterns:
            node = self.root
            for c in pattern:
                node = node.go[c]
            counts[pattern] = node.count
        return pos, counts


def naive_search(text: str, patterns: list[str]) -> tuple[dict[str, list[int]], dict[str, int]]:
    pos = {p: [] for p in patterns}
    cnt = {p: 0 for p in patterns}
    for p in patterns:
        start = 0
        while True:
            idx = text.find(p, start)
            if idx == -1:
                break
            pos[p].append(idx)
            cnt[p] += 1
            start = idx + 1
    return pos, cnt


alphabet = ['a', 'b', 'c']
for _ in range(1000):
    text = ''.join(random.choice(alphabet) for _ in range(random.randint(10, 1000)))
    patterns = list(set(''.join(random.choice(alphabet) for _ in range(random.randint(1, 10))) for _ in range(random.randint(1, 20))))
    ac = Trie()
    cur_pat = []
    for p in patterns:
        ac.add_pattern(p)
        cur_pat.append(p)
        ac_pos, ac_cnt = ac.search(text)
        naive_pos, naive_cnt = naive_search(text, cur_pat)
        assert ac_cnt == naive_cnt
        for p in cur_pat:
            assert sorted(ac_pos[p]) == sorted(naive_pos[p])

print("All tests passed!")
