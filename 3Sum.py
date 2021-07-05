def threeSum(nums):
    nums = sorted(nums)
    res = []
    for i in range(0, len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            lo = i + 1
            hi = len(nums) - 1
            summ = 0 - nums[i]

            while lo < hi:
                if nums[lo] + nums[hi] == summ:
                    tmp = [nums[i], nums[lo], nums[hi]]
                    res.append(tmp)

                    while (lo < hi and nums[lo] == nums[lo + 1]):
                        lo += 1
                    while (lo < hi and nums[hi] == nums[hi - 1]):
                        hi -= 1

                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < summ:
                    lo += 1
                else:
                    hi -= 1
    return res


print(threeSum([-1,0,1,2,-1,-4]))