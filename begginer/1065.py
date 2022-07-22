def ValoresPares():

    valores_pares = 0
    valores_impares = 0

    for i in range(5):
        i = int(input())

        if i % 2 == 0:
            valores_pares += 1

    return('%i valores pares' %(valores_pares))


a = ValoresPares()

print(a)