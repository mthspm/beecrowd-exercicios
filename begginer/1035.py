entrada = input()

entrada = entrada.split(" ")

A,B,C,D = int(entrada[0]), int(entrada[1]),int(entrada[2]),int(entrada[3])

if B > C and D > A and C+D > A+B and C > 0 and B > 0 and A%2 == 0:

    print('Valores aceitos')
else:
    print('Valores nao aceitos')