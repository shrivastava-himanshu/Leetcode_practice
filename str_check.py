def strStr(haystack, needle):
    if len(haystack) == 0 and len(needle) == 0: return(0)
    if len(haystack) > 0 and len(needle) ==0 : return(0)
    if haystack ==  needle: return(0)
    n_len = len(needle)
    for i in range(0,len(haystack)):
        if haystack[i:i+n_len] == needle:
            return i
    return(-1)


if __name__ == "__main__":
    haystack = "aafdasfasfdasdfz"
    needle = "z"
    print(strStr(haystack,needle))