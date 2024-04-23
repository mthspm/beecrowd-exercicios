N = int(input())
validation = False

while validation == False:

    if 1000000 > N and N > 0:
        validation = True

    else:
        validation = False
        N = int(input())

print(N)

cem = int(N / 100)
N = N % 100
    
cinquenta = int(N/50)
N = N % 50

vinte = int(N/20)
N = N % 20

dez = int(N/10)
N = N % 10

cinco = int(N/5)
N = N % 5

dois = int(N/2)
N = N % 2

um = N

print('%i nota(s) de R$ 100,00' %cem)

print('%i nota(s) de R$ 50,00' %cinquenta)

print('%i nota(s) de R$ 20,00' %vinte)

print('%i nota(s) de R$ 10,00' %dez)

print('%i nota(s) de R$ 5,00' %cinco)

print('%i nota(s) de R$ 2,00' %dois)

print('%i nota(s) de R$ 1,00' %um)