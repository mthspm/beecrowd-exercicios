salario = float(input())
cheker = False

if salario >= 0 and salario <= 2000:
    print('Isento')
    cheker = True

imposto = float

if cheker is False:
    if salario >= 2000.01 and salario <= 3000:
        salario = salario - 2000
        imposto = salario * 0.08

    elif salario >= 3000.01 and salario <= 4500:
        salario = salario - 3000
        imposto = (salario * 0.18) + 80

    elif salario > 4500:
        salario = salario - 4500
        imposto = (salario * 0.28) + 350

if cheker is False:
    print('R$ %.2f' %(imposto))