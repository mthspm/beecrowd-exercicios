def ValoresPositivos():

    positivos = 0
    positivos_lista = []
    media = 0

    for i in range(6):
        i = float(input())

        if i > 0 :
            positivos += 1
            positivos_lista += [i]
        
    for i in range(len(positivos_lista)):
        media += positivos_lista[i]

    media = media / len(positivos_lista)

    return('%i valores positivos\n%.1f' %(positivos,media))

a = ValoresPositivos()

print(a)