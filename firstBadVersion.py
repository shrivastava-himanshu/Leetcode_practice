def firstBadVersion(n):
    left, right  = 1, n

    while left < right:
        mid =  left + (right - left)+1
        if not isBadVersion(mid):
            left = mid+1
        else:
            right = mid

    return left



def isBadVersion(num):