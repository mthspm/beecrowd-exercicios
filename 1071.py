X,Y = int(input()),int(input())
soma = 0

if X < Y:
    a = X
    b = Y

elif X > Y:
    a = Y
    b = X

elif X == Y:
    a = 0
    b = 0

for i in range(a+1,b):
    if i % 2 != 0:
        soma += i

print(soma)

