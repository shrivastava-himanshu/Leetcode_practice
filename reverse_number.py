def reverse(self, x: int):
    rev = 0
    num = abs(x)
    while num != 0:
        dig = num % 10
        rev  = rev * 10 + dig
        num = num//10



    if x < 0:
        if abs(rev) > 2 ** 31 - 1:
            return(0)
        else:
            return(-abs(rev))
    else:
        if abs(rev) > 2 ** 31 - 1:
            return(0)
        else:
            return(abs(rev))



if __name__ == '__main__':
    x = 1563847412

    print(reverse(None,x))