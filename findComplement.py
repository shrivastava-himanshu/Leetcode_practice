def findComplement(num):
    res = []
    ori = []
    out = 0
    while num > 0:
        rem = num % 2
        #print(rem)
        num = num // 2
        ori.append(rem)
        if rem == 0:
            res.append(1)
        else:
            res.append(0)
    print(ori[::-1])
    print(res[::-1])
    for i in range(len(res)):
        out += res[i] * 2 ** i
    print(out)

findComplement(32)