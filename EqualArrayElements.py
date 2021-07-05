def minMoves(nums):
    sm = sum(nums)
    min_ele = min(nums)
    count = sm - (len(nums) * min_ele)
    return count



print(minMoves([1,1,1]))