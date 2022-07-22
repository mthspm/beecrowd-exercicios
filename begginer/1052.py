entrada = int(input())

meses = ['January','February','March','April','May','June','July','August','September','October','November','December']

resultado = ''

for i in range(1,13):
    if entrada == i:
        entrada = meses[i-1]

print(entrada)