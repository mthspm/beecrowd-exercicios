entrada = input()

entrada = entrada.split(" ")

x,y = float(entrada[0]), float(entrada[1])
posicao = ''

if x == 0 and y == 0:
    posicao = 'Origem'

elif x == 0 and y != 0:
    posicao = 'Eixo Y'

elif x != 0 and y == 0:
    posicao = 'Eixo X'

elif x > 0 and y > 0:
    posicao = 'Q1'

elif x < 0 and y > 0:
    posicao = 'Q2'

elif x < 0 and y < 0:
    posicao = 'Q3'

elif x > 0 and y < 0:
    posicao = 'Q4'

print(posicao)