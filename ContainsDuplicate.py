def containsDuplicate(nums):
    set_num = set(nums)

    if len(nums) > len(set_num):
        return True
    else:
        return False


print(containsDuplicate([1,2,3,4]))
