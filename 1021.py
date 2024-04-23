import math

N = float(input())
validation = False

while validation == False:

    if 1000000 > N and N > 0:
        validation = True

    else:
        validation = False
        N = float(input())

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

coin_1 = int(N/1)
N = N % 1

coin_05 = int(N/0.5)
N = N % 0.5

coin_025 = int(N/0.25)
N = N % 0.25

coin_010 = int(N/0.10)
N = N % 0.10

coin_005 = int(N/0.05)
N = N % 0.05

N = float('%.3f' %N)

coin_01 = int(N/0.01)

N = N % 0.01

print('NOTAS:')
print('%i nota(s) de R$ 100.00' %cem)
print('%i nota(s) de R$ 50.00' %cinquenta)
print('%i nota(s) de R$ 20.00' %vinte)
print('%i nota(s) de R$ 10.00' %dez)
print('%i nota(s) de R$ 5.00' %cinco)
print('%i nota(s) de R$ 2.00' %dois)

print('MOEDAS:')
print('%i moeda(s) de R$ 1.00' %coin_1)
print('%i moeda(s) de R$ 0.50' %coin_05)
print('%i moeda(s) de R$ 0.25' %coin_025)
print('%i moeda(s) de R$ 0.10' %coin_010)
print('%i moeda(s) de R$ 0.05' %coin_005)
print('%i moeda(s) de R$ 0.01' %coin_01)