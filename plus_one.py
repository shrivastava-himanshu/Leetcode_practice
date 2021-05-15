def plusOne(n):
    strings = [str(i) for i in n]
    a_string = "".join(strings)
    an_integer = int(a_string) + 1
    res = list(map(int, str(an_integer)))
    return (res)



if __name__ == "__main__":
    n = [9]
    plusOne(n)