valores = []

for i in range(6):
    i = float(input())
    valores += [i]

qtd_pos = 0

for i in valores:
    if i > 0:
        qtd_pos += 1

print('%i valores positivos' %(qtd_pos))