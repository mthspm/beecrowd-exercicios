def Intervalo():

    N = int(input())

    dentro = 0
    fora = 0

    for i in range(N):
        
        i = int(input())

        if i >= 10 and i <= 20:
            dentro +=1

        else:
            fora += 1

    return('%i in\n%i out' %(dentro,fora))

teste1 = Intervalo()

print(teste1)