entrada = input()

entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

hi,mi,hf,mf = entrada[0], entrada[1], entrada[2], entrada[3]

tt = 0

Ti = hi*60 + mi
Tf = hf*60 + mf

if Ti == Tf:
    tt = 24*60

if Ti > Tf:
    tt = abs((Tf+1440) - Ti)

if Tf > Ti:
    tt = abs(Tf-Ti)

horas_final = int(tt / 60)

minX = horas_final * 60

minutos_final = tt - minX

print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' %(horas_final,minutos_final))