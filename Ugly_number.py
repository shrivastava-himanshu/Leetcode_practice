def ugly_number(n):
    if n <= 0:
        return False
    factor = [2, 3, 5]
    for i in factor:
        while n % i == 0:
            n /= i
    return n == 1
'''    if num == 2 or num == 3 or num == 5 : return True
    ugly = 7
    num = abs(num)
    flag = True
    while ugly <= num // 2:
        if num % ugly == 0:
            flag = False
            break
        else:
            ugly += 1

    return flag
'''


if __name__ == "__main__":
    num = 0
    print(ugly_number(num))