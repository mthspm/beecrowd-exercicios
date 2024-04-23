def Quadrante():

    resultado = ''

    while True:

        entrada = input()

        entrada = entrada.split(" ")

        X,Y = int(entrada[0]), int(entrada[1])

        if X == 0 or Y == 0:

            break

        if X > 0 and Y > 0:
            resultado = 'primeiro'

        elif X > 0 and Y < 0:
            resultado = 'quarto'

        elif X < 0 and Y > 0:
            resultado = 'segundo'

        else:
            resultado = 'terceiro'

        print(resultado)

Quadrante()