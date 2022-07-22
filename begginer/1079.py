
N = int(input())
media = 0

for i in range(N):
    i = input()

    a = i.split(" ")
    
    n1 = float(a[0])
    n2 = float(a[1])
    n3 = float(a[2])

    media = (n1*2 + n2*3 + n3*5) / (10)

    print('%.1f' %media)