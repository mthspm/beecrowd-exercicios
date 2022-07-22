def VolEsfera(R):
    V = (4/3)*3.14159*R**3
    return V

r = float(input())

V1 = VolEsfera(r)

print('VOLUME = %.3f' %V1)


