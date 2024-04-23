entrada = input()
entrada = entrada.split(" ")

codigo,quantidade = int(entrada[0]),int(entrada[1])
preco = 0

for i in range(5):
    i = codigo

    if codigo == 1:
        preco = 4
    elif codigo == 2:
        preco = 4.5
    elif codigo == 3:
        preco = 5
    elif codigo == 4:
        preco = 2
    else:
        preco = 1.5

total = preco*quantidade

print('Total: R$ %.2f' %total)