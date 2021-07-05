def WordPattern(pattern,s):
    s_list = s.split()
    my_set = set()
    my_dict = {}
    if len(pattern) != len(s_list): return False

    for i in range(len(pattern)):
        x = pattern[i]
        y = s_list[i]

        if x in my_dict:
            if my_dict[x] != y:
                return False
        else:
            if y in my_set:
                return False

            my_dict[x] = y
            my_set.add(y)
    return True





print(WordPattern("abba","dog ct ct dog"))
