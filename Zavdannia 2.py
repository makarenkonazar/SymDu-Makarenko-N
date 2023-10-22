arr1 = []

for i in range(7):
    arr2 = []
    t = 7-i
    for j in range(7):
        if i > j:
            a = t+j
        else:
            a = 7-j+i

        arr2.append(a)

    arr1.append(arr2)

for i in arr1:
    print(*i)