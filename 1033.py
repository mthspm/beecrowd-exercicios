entrada = input()

entrada = entrada.split(" ")

def ChamaNota(x):
    return float(entrada[x])

N0,N1,N2,N3 = ChamaNota(0), ChamaNota(1), ChamaNota(2), ChamaNota(3)

media = (N0*2 + N1*3 + N2*4 + N3*1) / (10)

situacao = ''

if media >= 7:
    situacao = 'Aluno aprovado.'

    print('Media: %.1f' %media)
    print(situacao)

elif media >= 5 and media <= 6.9:
    situacao = 'Aluno em exame.'

    print('Media: %.1f' %media)
    print(situacao)
else:
    situacao = 'Aluno reprovado.'

    print('Media: %.1f' %media)
    print(situacao)

if situacao == 'Aluno em exame.':
    N_exame = float(input())

    media = (media + N_exame) / 2

    if media >= 5:
        situacao = 'Aluno aprovado.'
        print('Nota do exame: %.1f' %N_exame)
        print(situacao)
        print('Media final: %.1f' %media)
    else:
        situacao = 'Aluno reprovado.'
        print('Nota do exame: %.1f' %N_exame)
        print(situacao)
        print('Media final: %.1f' %media)