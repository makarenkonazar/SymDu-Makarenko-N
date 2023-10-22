def delete():

    A = list(map(int,input('Enter a list: ').split()))

    print(A)

    k = int(input('Enter element: '))

    result = []

    for x in range(len(A)):

        if A[x] != k:

            result.append(A[x])

    print(result)

    return result

delete()