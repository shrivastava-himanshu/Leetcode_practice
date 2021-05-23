def trailingZeroes(n):
    tz = 0
    five_power = 5
    while n//five_power > 0:
        tz += n//five_power
        five_power = five_power*5

    return tz



print(trailingZeroes(100))
