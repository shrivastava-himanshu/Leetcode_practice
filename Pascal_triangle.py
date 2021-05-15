def pascalTriangle(n):
    list_main = []
    for i in range(n):
        inner_list =[]
        for j in range(i+1):
            if j ==0  or j == i:
                inner_list.append(1)
            else:
                inner_list.append(list_main[i-1][j-1] + list_main[i-1][j])
        list_main.append(inner_list)

    return list_main[n-1]


if __name__ == "__main__":
    n = [7]
    for x in n:
        print(pascalTriangle(x))