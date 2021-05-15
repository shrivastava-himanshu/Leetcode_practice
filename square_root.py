def square_root(x):
    sqroot = x ** 0.5
    return(int(sqroot))

if __name__ == "__main__":
    x = [4,9]
    for i in x:
        print(square_root(i))
