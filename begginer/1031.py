entrada = float(input())

int1 = 'Intervalo [0,25]'
int2 = 'Intervalo (25,50]'
int3 = 'Intervalo [50,75]'
int4 = 'Intervalo (75,100]'

if entrada >= 0 and entrada <= 25:
    entrada = int1

elif entrada > 25 and entrada <= 50:
    entrada = int2

elif entrada > 50 and entrada <= 75:
    entrada = int3

elif entrada > 75 and entrada <= 100:
    entrada = int4

else:
    entrada = 'Fora de intervalo'

print(entrada)