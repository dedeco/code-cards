import sys
from typing import List


def min_and_max(arr: List) -> (int, int):
    max = - sys.maxsize - 1
    min = sys.maxsize
    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x
    return max, min


def min_and_max_2(arr: List) -> (int, int):
    max = - sys.maxsize - 1
    min = sys.maxsize
    for x in arr:
        if x < min:
            min = x
    for x in arr:
        if x > max:
            max = x
    return max, min


# Driver code
if __name__ == "__main__":
    arr = [54, 73, 2, 70, 73, 68, 52, 65, 99]
    max, min = min_and_max(arr)
    print(f'max: {max} min: {min}')
    max, min = min_and_max_2(arr)
    print(f'max: {max} min: {min}')
