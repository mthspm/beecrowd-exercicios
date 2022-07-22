A,B = float(input()), float(input())

A = float('%.2f' %A)
B = float('%.2f' %B)

#7.5 PESO = 68,18%
#3.5 PESO = 31,82%

MEDIA = (((A*3.5)+(B*7.5))/11)

MEDIA = float('%.5f' %MEDIA)

print('MEDIA = %.5f' %MEDIA)