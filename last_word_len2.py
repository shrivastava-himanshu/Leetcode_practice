def last_word_len(str):
    lis = list(str.split(" "))
    return len(lis[-1])

if __name__ == "__main__":
    str = ["Hello World", "Hello" , " "]
    for x in str:
        print(last_word_len(x))