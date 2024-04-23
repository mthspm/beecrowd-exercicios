from math import sqrt


P1,P2 = input(),input()

P1,P2 = P1.split(" "), P2.split(" ")

x1,y1 = float(P1[0]),float(P1[1])
x2,y2 = float(P2[0]),float(P2[1])

distancia = sqrt(((x2 - x1)**2) + ((y2-y1)**2))

distancia = float('%.4f' %distancia)

print(distancia)