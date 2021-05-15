def merge_arrays(A, m , B , n):
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0: # only iterating till b i.e lenght of second array because once the second array pointer reaches less then 1 , means all its values
        if a >= 0 and A[a] > B[b]:   # are placed in a sorted way in the first array and which is already sorted ... READ twice you will remember!!
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1

        write_index -= 1

    print(A)

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge_arrays(nums1,m,nums2,n)