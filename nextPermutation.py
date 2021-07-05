def nextPermutation(arr):
    n = len(arr) - 1
    if n <= 1: return
    for i in range(n, 0, -1):
        if arr[i] > arr[i - 1]:
            break
    first = i-1
    print(arr[first]," ",first)

    for j in range(n,i,-1):
        if arr[j] > arr[i-1]:
            second = j
            break

    print(arr[second]," ",second)

    arr[first],arr[second] = arr[second],arr[first]
    pre = arr[:first+1]
    post = arr[first+1:]
    post_rev = post[::-1]
    print(pre + post_rev)

nextPermutation([3,2,1])