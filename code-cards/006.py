def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Driver code
if __name__ == "__main__":
    assert fibonacci(10) == 55
