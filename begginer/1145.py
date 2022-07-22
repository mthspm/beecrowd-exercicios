def main():

    X,Y = map(int, input().split())

    linha = 0

    for i in range(Y):

        linha += 1

        if linha == X:
            print(i+1, end='\n')
            linha = 0
        else:
            print(i+1, end=' ')

main()