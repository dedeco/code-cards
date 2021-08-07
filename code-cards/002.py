def pair_sum_sequence(n: int) -> int:
    if n < 0:
        return 0
    return n + pair_sum_sequence(n - 1)


def pair_sum_sequence_2(n: int) -> int:
    sum_ = 0
    for i in range(n + 1):
        sum_ += i
    return sum_


# Driver code
if __name__ == "__main__":
    n = 5
    print(f"the sum of all numbers to {n} is {pair_sum_sequence(n)}")

    print(f"the sum of all numbers to {n} is {pair_sum_sequence_2(n)}")