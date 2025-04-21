import math, random
from typing import Literal
from bitarray import bitarray

class BloomFilter:
    def __init__(self, n, prob):
        self.prob = prob
        self.size = self.next_prime(int(-(n * math.log(prob))/(math.log(2)**2)))
        self.hashes = int((self.size / n) * math.log(2))
        self.storage = bitarray(self.size)
        self.hash_arrays = [[random.randint(0, self.size - 1) for _ in range(4)] for _ in range(self.hashes)]
    def next_prime(self, n: int) -> int:
        if n <= 1:
            return 2
        
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        i = n
        while True:
            if is_prime(i):
                return i
            i += 1
    
    def _hash(self, item: str, hash_array: list[int]) -> int:
        octets = list(map(int, item.split('.')))
        hash_val = 0
        for a, x in zip(hash_array, octets):
            hash_val += a * x
        return hash_val % self.size

    def insert(self, item: str) -> None:
        for hash_array in self.hash_arrays:
            self.storage[self._hash(item, hash_array)] = 1

    def __contains__(self, item: str) -> Literal[False]|Literal[True]:
        for hash_array in self.hash_arrays:
            if not self.storage[self._hash(item, hash_array)]:
                return False
        return True
