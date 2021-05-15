def searchInsert(nums, target):
    #if len(nums)
    for i in range(len(nums)):
        if target <= nums[i]:
            return(i)
            break
    return len(nums)



if __name__ == "__main__":
    nums = []
    tar = 7
    print(searchInsert(nums, tar))