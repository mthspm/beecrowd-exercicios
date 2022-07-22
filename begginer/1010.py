a,b = input(), input()

a,b = a.split(" "), b.split(" ")

npa = int(a[1])
vla = float(a[2])

npb = int(b[1])
vlb = float(b[2])

total = npa*vla + npb*vlb

print('VALOR A PAGAR: R$ %.2f' %total)