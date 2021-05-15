def roman_to_integer(rom_num):
    roman_dict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    i = 0
    int_num = 0
    while i < len(rom_num):
        s1 = roman_dict[rom_num[i]]
        if i+1 < len(rom_num):
            s2  = roman_dict[rom_num[i+1]]
            if s1 >= s2:
                int_num += s1
            else:
                int_num -= s1
            i += 1
        else:
            int_num += s1
            i += 1
    return(int_num)






if __name__ == '__main__':
    num = ['CXIV','III','IV','IX','LVIII','MCMXCIV']
    for i in num:
        print(roman_to_integer(i))