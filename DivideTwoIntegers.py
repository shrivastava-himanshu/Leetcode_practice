def divide(num,div):
    flag = 1
    quotient = 0
    if num < 0 and div > 0 : flag = -1
    elif num >0 and div <0 : flag = -1
    n,d = abs(num),abs(div)
    while n >= d:
        n -= d
        quotient += 1
        #print(n,"-",d)
    return flag * quotient


print(divide(-2147483648,-1))