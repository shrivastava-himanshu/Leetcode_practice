import math
def constructRectangle(area):
    l = 0
    w = 0
    if math.sqrt(area) == int(math.sqrt(area)):
        l = w = int(math.sqrt(area))
        return([l,w])
    else:
        w = int(math.sqrt(area))
        while (area % w != 0):
            w -= 1

        l = area // w

        return([l,w])


print(constructRectangle(5))