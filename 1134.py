def gastype():

    alcool = 0
    gas = 0
    diesel = 0

    while True:

        type = int(input())

        while True:

            if type < 1 or type > 4 :
                type = int(input())

            else:
                break

        if type == 1:
            alcool += 1

        elif type == 2:
            gas += 1

        elif type == 3:
            diesel += 1

        else:
            break

    print('MUITO OBRIGADO\nAlcool: %i\nGasolina: %i\nDiesel: %i' %(alcool,gas,diesel))

gastype()