from random import randint
class Node:
    def __init__(self, key: int):
        self.key = key
        self.prio = randint(1, 10**10)
        self.l = self.r = None
        self.f = key
        self.count = 1
        self.sum = key
    
class Treap:
    def __init__(self, arr: list[int] = []):
        self.root = None
        if arr:
            for i in arr:
                self.root = self.merge(self.root, Node(i))
    
    def cnt(self, node: Node) -> int:
        return node.count if node else 0
    
    def cur_sum(self, node: Node) -> int:
        return node.sum if node else 0
    
    def update(self, node: Node) -> None:
        if node:
            node.count = 1 + self.cnt(node.l) + self.cnt(node.r)
            node.sum = node.key + self.cur_sum(node.l) + self.cur_sum(node.r)
    
    def merge(self, left, right) -> Node:
        if not left or not right:
            return left if left else right
        if left.prio > right.prio:
            left.r = self.merge(left.r, right)
            self.update(left)
            return left
        else:
            right.l = self.merge(left, right.l)
            self.update(right)
            return right
    
    def splitBySize(self, node: Node, k: int) -> tuple[Node, Node]:
        if not node:
            return None, None
        if k <= self.cnt(node.l):
            LL, LR = self.splitBySize(node.l, k)
            node.l = LR
            self.update(node)
            return LL, node
        else:
            RL, RR = self.splitBySize(node.r, k - self.cnt(node.l) - 1)
            node.r = RL
            self.update(node)
            return node, RR

    def insert(self, pos, value) -> None:
        new_T = Node(value)
        if self.root is None:
            self.root = new_T
            return
        L, R = self.splitBySize(self.root, pos)
        self.root = self.merge(self.merge(L, new_T), R)

    def erase(self, pos, count=0) -> None:
        L, R = self.splitBySize(self.root, pos)
        E, RR = self.splitBySize(R, 1 if not count else count)
        self.root = self.merge(L, RR)

    def sum(self, f, to) -> int: 
        L, R = self.splitBySize(self.root, f)
        RL, RR = self.splitBySize(R, to - f + 1)
        res = self.cur_sum(RL)
        self.root = self.merge(L, self.merge(RL, RR))
        return res
    
def tests():
    treap = Treap()

    values = [10, 20, 30, 40, 50]
    for i, v in enumerate(values):
        treap.insert(i, v)

    assert treap.sum(0, 4) == sum(values)
    assert treap.sum(1, 3) == sum(values[1:4])
    assert treap.sum(0, 0) == values[0]
    assert treap.sum(4, 4) == values[4]

    treap.erase(2)
    expected = [10, 20, 40, 50]
    assert treap.sum(0, 3) == sum(expected)
    assert treap.sum(1, 2) == sum(expected[1:3])

    treap.erase(0)
    expected = [20, 40, 50]
    assert treap.sum(0, 2) == sum(expected)

    treap.insert(1, 25)
    expected = [20, 25, 40, 50]
    assert treap.sum(0, 3) == sum(expected)
    print("All tests passed!")
if __name__ == "__main__":
    tests()
