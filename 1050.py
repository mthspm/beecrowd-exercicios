DDD = int(input())

DDD_LIST = [61,71,11,21,32,19,27,31]

pertence = False

dest = ''

if DDD in DDD_LIST:
    pertence = True
else:
    print('DDD nao cadastrado')

if DDD == 61:
    dest = 'Brasilia'
elif DDD == 71:
    dest = 'Salvador'
elif DDD == 11:
    dest = 'Sao Paulo'
elif DDD == 21:
    dest = 'Rio de Janeiro'
elif DDD == 32:
    dest = 'Juiz de Fora'
elif DDD == 19:
    dest = 'Campinas'
elif DDD == 27:
    dest = 'Vitoria'
elif DDD == 31:
    dest = 'Belo Horizonte'

if pertence is True:
    print(dest)