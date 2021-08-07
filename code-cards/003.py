from typing import List


def add_runtime(A: List, B: List):
    for i in A:
        print(i)
    for j in B:
        print(j)


def multiply_runtime(A: List, B: List):
    for i in A:
        for j in B:
            print(f'{i} + {j}')


# Driver code
if __name__ == "__main__":
    A = range(1, 10)
    B = range(1, 100)

    add_runtime(A, B)
    multiply_runtime(A, B)
