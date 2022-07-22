Entrada = input()

Entrada = Entrada.split(" ")

A,B,C = float(Entrada[0]), float(Entrada[1]), float(Entrada[2])

Area_triangulo = (A*C)/2
Area_circulo = (3.14159)*(C**2)
Area_trapezio = ((A+B)*C)/2
Area_quadrado = B**2
Area_retangulo = A*B

print('TRIANGULO: %.3f' %Area_triangulo)
print('CIRCULO: %.3f' %Area_circulo)
print('TRAPEZIO: %.3f' %Area_trapezio)
print('QUADRADO: %.3f' %Area_quadrado)
print('RETANGULO: %.3f' %Area_retangulo)

