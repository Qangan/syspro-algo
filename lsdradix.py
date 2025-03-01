import random, string

def gen_string(leng: int) -> str:
    return ''.join(random.choice(string.printable) for i in range(leng))

def c_sort(strs: list[str], index: int) -> None:
    strc, strl = len(strs), len(strs[0])
    res = [0] * strc
    c_arr = [0] * 128

    for i in range(strc):
        sym_ind = ord(strs[i][strl - index])
        c_arr[sym_ind] += 1
    
    for i in range(1, 128):
        c_arr[i] += c_arr[i - 1]

    for i in range(strc - 1, -1, -1):
        sym_ind = ord(strs[i][strl - index])
        res[c_arr[sym_ind] - 1] = strs[i]
        c_arr[sym_ind] -= 1
    
    for i in range(strc):
        strs[i] = res[i]

def lsd_radix_sort(array: list[str]) -> list:
    leng = len(array[0])
    dig = 1
    while dig <= leng:
        c_sort(array, dig)
        dig += 1
    return array

for i in range(100):
    sorting_arr = [gen_string(10) for i in range(100)]
    if lsd_radix_sort(sorting_arr) != sorted(sorting_arr):
        print("TEST IS NOT PASSED")

print("All tests passed!")

