from bloomfilter import BloomFilter
import random

bloom = BloomFilter(20, 0.5)
ips = [
    "182.12.2.2",
    "12.12.11.1",
    "234.121.11.1",
    "100.20.2.6",
    "8.8.8.8",
    "123.123.123.123",
    '1.1.1.1',
    '34.23.63.12',
    '93.21.22.22'
]
for i in ips:
    bloom.insert(i)
a = [f"{str(random.randint(0, 255))}.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}" for _ in range(100000)]
z = 0
for i in a:
    if i in bloom:
        if i not in ips:
            z += 1
        else:
            print("True:", i)
print(z/100000)
