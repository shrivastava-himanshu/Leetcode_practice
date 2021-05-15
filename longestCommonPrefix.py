def min_lenght(strs):
    i = 0
    min_len = len(strs[i])
    for i in strs:
        if len(i) < min_len:
            min_len = len(i)  # can be optimized by sorting the list and then the first string length
    return min_len


def longestCommonPrefix(strs):
    ln =  min_lenght(strs)
    prefix = ""

    for i in range(ln):
        current_pre = strs[0][i]
        for j in range(1,len(strs)):
            if strs[j][i] != current_pre:
                return prefix
        prefix = prefix + current_pre

    return prefix


if __name__ == "__main__":
    strs = [["flower","flow","flight"],
            ["dog", "dogcar", "doggycar"]]
    #longestCommonPrefix(strs)
    for x in (strs):
        print(longestCommonPrefix(x))