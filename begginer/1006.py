def Input():
    y = float(input())
    y = float('%.1f' %y)
    return y

A,B,C = Input(), Input(), Input()

TOTAL = (A*2) + (B*3) + (C*5)

MEDIA = TOTAL / 10

MEDIA = float('%.1f' %MEDIA)

print('MEDIA = %.1f' %MEDIA)

