def isHappy(n):
    tx = 0
    if n ==1 or n==7: return False
    while n > 9:
        tx += (n % 10) ** 2
        n = n // 10
    if  tx != 1:
        return isHappy(tx)
    else:
        return True


print(isHappy(2))