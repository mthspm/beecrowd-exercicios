N = int(input())

resultado = ' '

for i in range(N):
    i = int(input())

    if i % 2 == 0 and i != 0:
        resultado = 'EVEN'
    elif i % 2 != 0:
        resultado = 'ODD'
    else:
        resultado = 'NULL'
    
    if resultado != 'NULL' and i > 0:
        resultado += ' POSITIVE'

    elif resultado != 'NULL' and i < 0:
        resultado += ' NEGATIVE'

    print(resultado)