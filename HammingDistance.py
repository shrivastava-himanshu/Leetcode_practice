def hamming_distance():
    x = [1,0,0,1,1]
    y = [0,0,0,1]
    count = 0
    for i in range(len(x)):
        if (x[i] ^ y[i]) != 0:
            count += 1
    print(count)



hamming_distance()