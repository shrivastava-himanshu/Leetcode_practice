def longestSubStr(str):
    #sub = []
    last_idx = {}
    max_len = 0
    start_idx = 0
    prev_len = curr_len = 0
    for i in range(len(str)):
        if str[i]  in last_idx:
            start_idx = max(start_idx,last_idx[str[i]]+1)

        max_len = max(max_len,i-start_idx +1)
        last_idx[str[i]] = i

    return max_len


    '''     sub.append(str[i-1])
            i += 1
        else:
            sub = [str[i-1]]
            curr_len = 0
            i += 1
        if prev_len < len(sub):
            prev_len = len(sub)
    return (sub, " " ,prev_len)
    '''

print(longestSubStr('dvdf'))