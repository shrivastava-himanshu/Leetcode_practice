def trailingZeroes(n):
    fact = factorial(n)
    count = 0
    if fact == 0: return 0
    while fact % 10 == 0:
        count += 1
        fact = fact // 10
    return (count)


def factorial(n):
    if n == 1:
        return n
    elif n <= 0:
        return (0)
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(trailingZeroes(20))