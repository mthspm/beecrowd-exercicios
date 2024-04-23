entrada = input()

entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

ti,tf,tt = entrada[0], entrada[1], 0

if ti == tf:
    tt = 24

if ti > tf:
    tt = abs((tf+24) - ti)

if tf > ti:
    tt = abs(tf-ti)

print('O JOGO DUROU %i HORA(S)' %tt)