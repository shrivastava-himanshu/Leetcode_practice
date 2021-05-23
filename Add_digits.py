def add_digits(num: int):
    sum = 0
    if num < 10:
        return(num)
    else:
        for i in str(num):
            sum += int(i)
        return(add_digits(sum))

#    return sum
'''
Method # 2 :

def add_digits(num: int):
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum < 10:
        return(int(sum))
    else:
        return(add_digits(sum))



'''


if __name__ == "__main__":
    print(add_digits(12345))