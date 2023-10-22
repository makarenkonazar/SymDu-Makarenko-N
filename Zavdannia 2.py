def average():

    A = list(map(int,input('Enter a list: ').split()))

    print(A)

    sum_vid = 0
    count = 0

    for i in range(len(A)):
        if A[i] < 0:
            sum_vid += A[i]
            count += 1

    avr = sum_vid / count

    print ('Average is:',avr)

    return avr

average()