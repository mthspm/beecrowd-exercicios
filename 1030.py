import math

entrada = input()

entrada = entrada.split(" ")

A,B,C = float(entrada[0]), float(entrada[1]), float(entrada[2])

#delta = b**2 - 4.a.c

delta = (B**2) - (4*A*C)

#x = -b +- sqrt(delta) / 2a

delta_valid = True

if delta == 0 or delta < 0:
    print('Impossivel calcular')
    delta_valid = False

if delta_valid == True and A != 0:

    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)

    print('R1 = %.5f' %x1)
    print('R2 = %.5f' %x2)

elif A == 0:
    print('Impossivel calcular')