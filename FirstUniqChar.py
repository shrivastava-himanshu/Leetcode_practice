def firstUniqChar(s):
    dict_s = {}
    counter = []
    for i in s:
        if i in dict_s:
            dict_s[i] += 1
        else:
            dict_s[i] = 1

    for i in range(len(s)):
        if dict_s[s[i]] == 1:
            return s[i]

    return -1


print(firstUniqChar('leetcode'))