def canConstruct(ransom,magazine):
    r_str = list(ransom)
    m_str = list(magazine)
    i = 0
    for i in range(len(r_str)-1):
        if r_str[i] in m_str:
            m_str.remove(r_str[i])
            i += 1
            flag = True
        elif r_str[i] not in m_str:
            flag = False
    return flag





if __name__ == "__main__":
    print(canConstruct("aa","ab"))