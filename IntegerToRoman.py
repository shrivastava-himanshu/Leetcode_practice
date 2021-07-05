def IntToRoman(num):
    num_dict = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
              50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}

    int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #numbs in descending order as Numeric values go from Thousand, Hundred,Tens, Ones
    roman = ''
    for n in int_num:
        if num != 0:
            quotient = num // n
            if quotient != 0:
                for y in range(quotient):
                    roman += num_dict[n]
            num = num % n

    return roman

print(IntToRoman(3999))