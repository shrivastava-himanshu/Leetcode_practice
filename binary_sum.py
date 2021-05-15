def binarySum(a,b):
    sum = bin(int(a,2)+ int(b,2))
    return sum[2:]

if __name__ == "__main__":
    a = "1010"
    b = "1001"
    print(binarySum(a,b))