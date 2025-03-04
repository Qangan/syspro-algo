import random

def gen_string(leng: int) -> list:
    seq = range(10000)
    return [random.choice(seq) for _ in range(leng)]

def part(arr: list[int], l: int, h: int) -> int:
    def _part(arr: list[int], l: int, h: int) -> int:
        pivot = arr[l]
        i, j = l - 1, h + 1
        while True:
            while True:
                i += 1
                if not (i < j and arr[i] < pivot):
                    break
            while True:
                j -= 1
                if not (j >= 1 and arr[j] >= pivot):
                    break
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                return j

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
    if sorted(arr)[l//2] != kth(arr, l//2):
        print("TEST NOT PASSED", sorted(arr), kth(arr, l // 2))
        quit()
print("All tests passed!")
