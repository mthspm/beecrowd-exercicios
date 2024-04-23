def logic():

    N = int(input())

    a = 1
    b = 1
    c = 1
    saida = 0

    b2 = 0
    parametro = 2


    for i in range(N*2):

        print(a,b,c)
        
        #A
        if saida%2 != 0:    #saida IMPAR
            a += 1

        saida += 1

        #B
        if saida%2 != 0:   #SAIDA IMPAR
            b += 1
            c += 1

        elif saida%2 == 0:  #SAIDA PAR
            b2 += 2
            b += b2
            
            c = b*parametro
            parametro += 1

logic()