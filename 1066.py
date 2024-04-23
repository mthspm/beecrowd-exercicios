def NaturezadosValores():

    valores_pares = 0
    valores_impares = 0
    valores_positivos = 0
    valores_negativos = 0

    for i in range(5):
        i = int(input())

        if i % 2 == 0:
            valores_pares += 1

        else:
            valores_impares += 1


        if i > 0:
            valores_positivos += 1
        
        elif i < 0:
            valores_negativos += 1

    return('%i valor(es) par(es)\n%i valor(es) impar(es)\n%i valor(es) positivo(s)\n%i valor(es) negativo(s)' %(valores_pares,valores_impares,valores_positivos,valores_negativos))


a = NaturezadosValores()

print(a)