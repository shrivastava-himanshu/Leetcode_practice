def climbStairs(n):
    #fibonacci
    x,y = 1,1
    for i in range(2,n+1):
        x,y = y, x+y
    return y


print(climbStairs(30))