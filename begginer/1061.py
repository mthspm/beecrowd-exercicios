ent1,ent2,ent3,ent4 = input(), input(), input(), input()

ent1 = ent1.split(" ")
ent2 = ent2.split(" : ")
ent3 = ent3.split(" ")
ent4 = ent4.split(" : ")

dia_i = int(ent1[1])

hora_i = int(ent2[0])
min_i = int(ent2[1])
seg_i = int(ent2[2])

dia_f = int(ent3[1])

hora_f = int(ent4[0])
min_f = int(ent4[1])
seg_f = int(ent4[2])

Ti  = (dia_i*3600*24)+(hora_i*60*60)+(min_i*60)+(seg_i) #tempo inicial em segundos

Tf = (dia_f*3600*24)+(hora_f*60*60)+(min_f*60)+(seg_f) #tempo final em segundos

TempoTotal = Tf-Ti

dias = TempoTotal / 86400

TempoNovo = TempoTotal % 86400

horas = TempoNovo / 3600
TempoNovo %= 3600

minutos = TempoNovo / 60
TempoNovo %= 60

segundos = TempoNovo % 60

print('%i dia(s)' %dias)
print('%i hora(s)' %horas)
print('%i minuto(s)' %minutos)
print('%i segundo(s)' %segundos)