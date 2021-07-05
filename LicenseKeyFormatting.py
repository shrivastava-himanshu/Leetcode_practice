def licenseKeyformatting(s,k):
    n = s.replace('-','').upper()
    res = []
    length = len(n)
    if length % k !=0:
        res.append(n[:length%k])
        n = n[length%k:]
        length = len(n)

    for i in range(0,length,k):
        res.append(n[i:i+k])
    return '-'.join(res)


print(licenseKeyformatting("2-5g-3-J",2))