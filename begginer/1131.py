def main():

    jogos = 0
    interwin = 0
    grewin = 0
    draw = 0
    morewin = ''

    while True:

        first_input = input()

        first_input = first_input.split(" ")

        A,B = int(first_input[0]), int(first_input[1])  # A = INTER , B = GREMIO

        jogos += 1

        if A > B:
            interwin += 1
        elif A < B:
            grewin += 1
        else:
            draw += 1

        print('Novo grenal (1-sim 2-nao)')

        second_input = int(input())

        if second_input == 2:
            break
        else:
            continue

    if interwin > grewin:
        morewin = 'Inter venceu mais'
    elif interwin < grewin:
        morewin = 'Gremio venceu mais'
    else:
        morewin = 'Nao houve vencedor'

    print('%i grenais\nInter:%i\nGremio:%i\nEmpates:%i\n%s' %(jogos,interwin,grewin,draw,morewin))

main()