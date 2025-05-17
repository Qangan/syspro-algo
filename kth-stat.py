import random

def gen_string(leng: int) -> list:
    seq = range(10000)
    return [random.choice(seq) for _ in range(leng)]

def part(arr: list[int], l: int, h: int) -> int:
    def _part(arr: list[int], l: int, h: int) -> int:
        pivot = arr[h]
        i = l
        for j in range(l, h):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1 
        arr[i], arr[h] = arr[h], arr[i]
        return i
    r = random.randint(l, h)
    arr[r], arr[l] = arr[l], arr[r]
    return _part(arr, l, h)
    
def kth(array: list[int], k: int):
    if len(array) == 1:
        return array[0]

    p = part(array, 0, len(array) - 1)

    if p + 1 == k:
        return array[p]
    elif p + 1 > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)

def solution(arr: list[int]):
    return kth(array, len(array) // 2)

for i in range(1000):
    arr = gen_string(i), 
    l = len(arr) - 1
    if sorted(arr)[l // 2] != kth(arr, l // 2):
        print("TEST NOT PASSED", sorted(arr), kth(arr, l // 2))
        quit()
print("All tests passed!")
