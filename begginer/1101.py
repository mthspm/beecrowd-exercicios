def seqNumSum():

    while True:

        entrada = input()

        entrada = entrada.split(" ")

        beta = []

        soma = 0

        a = ''

        b = ''

        M,N = int(entrada[0]),int(entrada[1])

        if M <= 0 or N <= 0:
            break

        if M < N:
            A = M
            B = N
        else:
            A = N
            B = M
        
        for i in range(A,B+1):

            beta += [i]

        for i in range(len(beta)):

            soma += int(beta[i])

            a = '%i ' %beta[i]

            b += a
        
        print('%sSum=%i' %(b,soma))

seqNumSum()