def sum13(nums):
    s = sum(nums)
    i = 0
    while i<=len(nums)-1:

        if nums[i] == 13 and i == len(nums) - 1:
            s = s - nums[i]   #- nums[i+1]
            i += 1
        elif nums[i] == 13 and i != len(nums) - 1:
            s = s - nums[i] - nums[i + 1]
            i += 2
        else:
            i +=1

    return (s)


if __name__ == '__main__':
    a = [1,2,2,1]
    print(sum13(a))