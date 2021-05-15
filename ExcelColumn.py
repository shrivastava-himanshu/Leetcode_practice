def ExcelColumn(n):
    col_str = ''
    while n > 0 :
        index = (n-1)%26
        col_str += chr(index + ord('A'))
        n = (n-1) // 26

    return col_str[::-1]


print(ExcelColumn(70321))