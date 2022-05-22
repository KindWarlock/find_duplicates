import os
import time
import random
    

def gen_R():
    _R = {}
    n = 256
    nums = [i for i in range(10 ** 5)]
    for i in range(n):
        value = random.choice(nums)
        _R[i] = value
        nums.remove(value)
    return _R


def find_duplicates(files, hash_function):
    start_time = time.time()
    unique = set()
    for i in files:
        unique.add(hash_function(i))
    end_time = time.time()
    return end_time - start_time, list(unique)


def CRC(file):
    h = 0
    for i in range(len(file)):
        ki = ord(file[i])
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = h ^ ki
    return h


def PJW(file):
    h = 0
    for i in range(len(file)):
        ki = ord(file[i])
        h = (h << 4) + ki
        g = h & 0xf0000000
        if g != 0:
            h = h ^ (g >> 24)
            h = h ^ g
    return h


def BUZ(file):
    h = 0
    for i in range(len(file)):
        ki = ord(file[i])
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R[ki]
    return h


def read_all_files(dir_path: str):
    files = []
    for filename in os.listdir(dir_path):
        with open(os.path.join(dir_path, filename), 'r') as f:
            lines = f.read()
            files.append("".join(lines.split()))
    return files


path = "./out"
arr = read_all_files(path)
R = gen_R()

for hash_f in [CRC, PJW, BUZ]:
    comp_time, no_dupl = find_duplicates(arr, hash_f)
    print(f"{hash_f.__name__}:")
    print(f"    Time: {comp_time}")
    print(f"    Number of duplicates: {len(arr)-len(no_dupl)}\n")