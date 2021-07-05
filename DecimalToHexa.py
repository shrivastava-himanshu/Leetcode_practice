import math


def toHex( num):
    chars = '0123456789abcdef'
    ret = []
    if num < 0:
        num = math.pow(2, 32) - abs(num)
    while num > 0:
        ch = chars[int(num % 16)]
        ret.insert(0, ch)
        num //= 16
    return ''.join(ret) or '0'



print(toHex(-1))
'''
def decTohex(num):
    hex_dict ={
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    res = ''
    hexa = []
    sign = ''
    if num < 0:
        sign = '-'
        #num = abs(num)
    while num:
        rem =  num % 16
        num = num // 16
        hexa.append(rem)
    hexa = hexa[::-1]
    #print(hexa)
    for i in hexa:
        if i in hex_dict:
            res += hex_dict[i]
        else:
            res += str(i)
    print(sign+res)

decTohex(-1)

'''