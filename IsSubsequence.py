
def isSubSequence(str_a,str_b):
    i = j = 0
    while i < len(str_a) and j < len(str_b):
        if str_a[i]  == str_b[j]:
            i += 1
        j += 1
    return i == len(str_a)


    '''
    
    This works for 13/16 Test Cases
    my_dict = {}
    b_list = list(str_b)
    if str_a == "": return True
    for i in range(len(str_a)):
        if str_a[i] in str_b:
            my_dict[str_a[i]] = b_list.index(str_a[i])
        else:
            return False

    if list(my_dict.values()) == sorted(my_dict.values()):
        return True
    else: return False
    '''
print(isSubSequence("aaaa","aaaabb"))