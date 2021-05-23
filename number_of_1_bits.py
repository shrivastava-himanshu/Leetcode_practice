def hammingWeight(n:int) -> int :
    c = 0
    while n != 0:
        c += n % 2
        n = n // 2
    return c

print(hammingWeight(00000000000000000000000000001011))