def mergeTwoLists(l1, l2):
    len_a = len(l1)
    len_b = len(l2)
    arr = []
    print(arr)
    i = j = k = 0
    while i < len_a and j < len_b:
        if l1[i] < l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = l1[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = l2[j]
        j += 1
        k += 1
    print(arr)


if __name__ == '__main__':
    l1 = [1,2,3]
    l2 = [1,4,5]
    mergeTwoLists(l1 , l2)