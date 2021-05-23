def checkDuplicatesWithinK(num, k):
    my_set = {}
    for i in range(len(num)):
        if num[i] in my_set:
            if i - my_set[num[i]] <= k:
                return True
            my_set[num[i]] = i
        else:
            my_set[num[i]] = i
    return False




# Driver Code
if __name__ == "__main__":

    arr = [99,99]
    n = len(arr)
    print(checkDuplicatesWithinK(arr, 2))
