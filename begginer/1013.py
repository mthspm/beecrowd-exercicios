entrada = input()

entrada = entrada.split(" ")

a,b,c = int(entrada[0]), int(entrada[1]), int(entrada[2])

if a > b and a > c:
    print('%i eh o maior' %a)

elif b > a and b > c:
    print('%i eh o maior' %b)

elif c > a and c > b:
    print('%i eh o maior' %c)

elif b == a and b > c:
    print('%i eh o maior' %b)

elif b == a and c > b:
    print('%i eh o maior' %c)

elif b == c and b > a:
    print('%i eh o maior' %b)

elif b == c and a > b:
    print('%i eh o maior' %a)

elif b == c and c == a:
    print('%i eh o maior' %a)