iden1, iden2, iden3 = input(), input(), input()

result = ''
cheker = False

while cheker is False:
    
    if iden1 == 'vertebrado':

        if iden2 == 'ave':
            
            if iden3 == 'carnivoro':
                result = 'aguia'
                cheker = True

            elif iden3 == 'onivoro':
                result = 'pomba'
                cheker = True

        elif iden2 == 'mamifero':

            if iden3 == 'onivoro':
                result = 'homem'
                cheker = True

            elif iden3 == 'herbivoro':
                result = 'vaca'
                cheker = True

    else:
        break

if cheker == False:

    if iden1 == 'invertebrado':

        if iden2 == 'inseto':
            
            if iden3 == 'hematofago':
                result = 'pulga'

            elif iden3 == 'herbivoro':
                result = 'lagarta'

            
        elif iden2 == 'anelideo':

            if iden3 == 'hematofago':
                result = 'sanguessuga'

            elif iden3 == 'onivoro':
                result = 'minhoca'

print(result)