from typing import List


def binary_search_iterative(arr: List, number: int):
    left = 0
    right = len(arr) - 1
    middle = 0
    while left <= right:
        middle = left + (right - left) // 2
        print('middle', middle, 'left', left, 'right', right)
        if arr[middle] == number:
            print(f'{arr[middle]} == {number}')
            return middle
        elif arr[middle] > number:
            print(f'{arr[middle]} > {number} verdadeiro')
            right = middle - 1
        else:
            print(f'{arr[middle]} > {number} dá falso')
            left = middle + 1
    return -1


# Driver code
if __name__ == "__main__":
    arr = [2, 3, 5, 10, 40, 50, 60, 70, 100]
    x = 10

    result = binary_search_iterative(arr, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
