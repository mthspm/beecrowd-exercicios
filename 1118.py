def main():

    def notavalida(nota):

        if nota >= 0 and nota <= 10:
            return True

        else:
            return False

    media = 0
    Prova1 = float(input())

    while True:
        
        if notavalida(Prova1) is False:
            print('nota invalida')
            Prova1 = float(input())

        elif notavalida(Prova1) is True:
            media += Prova1
            break

    Prova2 = float(input())

    while True:
    
        if notavalida(Prova2) is False:
            print('nota invalida')
            Prova2 = float(input())

        elif notavalida(Prova2) is True:
            media += Prova2
            break

    media = media / 2
    print('media = %.2f' %media)
    response = bool

    while True:

        print('novo calculo (1-sim 2-nao)')

        new_calculo = int(input())

        if new_calculo == 1:
            return True
        
        elif new_calculo == 2:
            exit()

        else:
            continue

while True:

    a = main()

    if a is True:
        continue

    else:
        exit()