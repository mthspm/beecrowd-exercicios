def CrescDecresc():

    while True:

        entrada = input()

        entrada = entrada.split(" ")

        X,Y = int(entrada[0]),int(entrada[1])

        if X == Y:
            break

        if X > Y:
            print('Decrescente')

        else:
            print('Crescente')

CrescDecresc()

