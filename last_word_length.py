def last_word_length(s):
    count = 0
    #rev_str = str[::-1]
    x = s.strip()

    for i in range(len(x)):
        if x[i] == " ":
            count = 0
        else:
            count += 1
    return count


if __name__ == "__main__":
    str = ["Hello World", "Hello " , " "]
    for x in str:
        print(last_word_length(x))