def perfectSquare(num):
    rem = 1
    while (num - rem ** 2)>=0:
        if num - rem ** 2 == 0:
            return True
            break
        rem += 1

    return False



print(perfectSquare(0))
