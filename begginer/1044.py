entrada = input()

entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

A,B = entrada[0],entrada[1]

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')