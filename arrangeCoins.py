def arrangeCoins(n: int) -> int:
    count = 0
    s = 0
    e = n
    while (s <= e):

        m = (s + e) // 2

        count = (m * (m + 1)) // 2

        if count == n:
            return m
        elif count < n:
            s = m + 1
        else:
            e = m - 1
    return e

print(arrangeCoins(6))







'''
def arrangeCoins(n):
    count = 0
    i = 1
    while n >= i:
        if n-i >= 0:
            count += 1
        n = n-i
        i += 1

    print(count)

arrangeCoins(3)
'''