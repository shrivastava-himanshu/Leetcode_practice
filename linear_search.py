def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        print("k = %d",k)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print("checking arr[k] in L[i]")
            print(k)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()


if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7, 8]
	print("Given array is", end="\n")
	printList(arr)
	merge_sort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)