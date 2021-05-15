def removeElement(nums, value):
    if len(nums) <2 : return ("single element array")
    i = -1
    for j in range(0,len(nums)):
        if nums[j] == value:
            continue
        i += 1
        if i != j:
            nums[i] = nums[j]
    return i+1

if __name__ == "__main__":
    nums = [3,2,2,3]
    nums2 = [0,1,2,2,3,0,4,2]
    val1 = 3
    val2 = 2
    print(removeElement(nums,val1))
    print(removeElement(nums2,val2))
