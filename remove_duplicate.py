def removeDuplicates(num):
    if len(num) < 2: return len(num)

    i = 0 # slow pointer for 2 pointer approach
    for j in range(1,len(num)):
        if num[j] ==  num[i]:  #checks for same number  and if same then move to next
            continue
        i += 1
        if i != j:
            num[i] = num[j]   # if the number is same and index is different then in place over ride the value on index i (slower index)

    return i+1



if __name__ == "__main__":
    num = [0, 0, 1 , 1, 1, 2,2,2,2,2,2,2,2,2,3,3,4,4,5]
    #for i in num:
    print(removeDuplicates(num))