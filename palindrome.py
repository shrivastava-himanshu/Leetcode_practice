def palindrome(x):
    if x >= 0:
        rev = 0
        num = abs(x)
        while num != 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if x == rev:
            return ('true')
        else:
            return ('false')
    else:
        return('false')

if __name__ == '__main__':

    x = [-23232 , 121, 10, -101]
    for i in (x):
        print(palindrome(i))

