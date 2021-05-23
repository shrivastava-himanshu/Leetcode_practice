def mising_number(n):
    sum = 0
    for i in n:
        sum += i
    l = len(n)
    true_sum = (l * (l + 1) ) // 2
    return(abs(sum - true_sum))



x = [9,6,4,2,3,5,7,0,1]
print(mising_number(x))