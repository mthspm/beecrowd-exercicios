def QuadradodePares():

    N = int(input())

    if N < 5 or N > 2000:
        N = int(input())

    for i in range(N+1):

        if i % 2 == 0 and i != 0:
            print('%i^2 = %i' %(i,i**2))

QuadradodePares()