def ExcelColumn(n):
    pow = 1
    col_num = 0
    for x in n[::-1]:
        col_num += (int(x,36)-9) * pow
        pow *=26


    return col_num

print(ExcelColumn('ZY'))