from collections import Counter

def findTheDiff(s,t):
    if s == '' or  t == '':
        return s if s!="" else t
    elif len(set(s)) != len(set(t)):
        return list(set(t).difference(set(s)))[0]
    else:
        c1,c2 = Counter((s)),Counter((t))
        for i in c1:
            if c1[i] != c2[i]:
                return i



print(findTheDiff('a','aabcde'))