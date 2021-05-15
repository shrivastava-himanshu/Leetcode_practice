def maximum_subarray(nums):
    max_so_far = 0
    max_current = 0
    all_neg = True

    for i in range(0, len(nums)):
        max_current += nums[i]
        if nums[i] > 0:
            all_neg = False
        if max_current > max_so_far:
            max_so_far = max_current
        elif max_current < 0:
            max_current = 0
    if all_neg == True:
        return sum(nums)
    return max_so_far

if __name__ == '__main__':
    nums = [-5,-4,-1,-7,-8]
    print(maximum_subarray(nums))