entrada = input()

entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = float(entrada[i])

A,B,C = entrada[0],entrada[1],entrada[2]

'''
| b - c | < a < b + c
| a - c | < b < a + c                             //Condicao de existencia de um triangulo
| a - b | < c < a + b
'''
condicao_triangulo = bool
Perimetro_triangulo = 0
Area_trapezio = 0


if abs(B-C) < A and A < B+C and abs(A-C) < B and B < A+C and abs(A-B) < C and C < A+B:
    condicao_triangulo = True
else:
    condicao_triangulo = False

if condicao_triangulo == True:
    Perimetro_triangulo = A+B+C
    print('Perimetro = %.1f' %Perimetro_triangulo)
else:
    Area_trapezio = ((A+B)*C)/(2)
    print('Area = %.1f' %Area_trapezio)