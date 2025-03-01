import random

def gen_string(leng: int) -> list:
    seq = range(3)
    return [random.choice(seq) for _ in range(leng)]

def sortColors(nums: list[int]) -> None:
        sort_dict = [0, 0, 0]
        for i in nums:
            sort_dict[i] += 1
        ind = 0
        for i in range(3):
            for j in range(sort_dict[i]):
                nums[ind] = i
                ind += 1
        return nums

for i in range(100):
    sorting_arr = gen_string(i)
    if sortColors(sorting_arr) != sorted(sorting_arr):
        print("TEST IS NOT PASSED")

print("All tests passed!")
