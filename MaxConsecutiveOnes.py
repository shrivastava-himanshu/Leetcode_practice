"""
def maxOnes(nums):
    count,i = 0,0
    max_count = 0
    while i<len(nums):
        if nums[i] == 1:
            count +=1
        elif nums[i] != 1:
            count =0

        if count > max_count:
            max_count = count
        i += 1

    print(max_count)



maxOnes( [])

"""
"""
Clever solutions
Using multiplication as the input will only have 1's and 0's
if anything multiplied by 0 will turn it to 0
"""


def findMaxConsecutiveOnes(nums):
    consecutive = result = 0
    for n in nums:
        consecutive = consecutive * n + n
        result = max(result, consecutive)
    return result


print(findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,1,1]))