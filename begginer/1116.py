def main():

        N = int(input())

        for i in range(N):

            entrada = input()

            entrada = entrada.split(" ")

            X,Y = int(entrada[0]),int(entrada[1])

            if Y == 0:
                print('divisao impossivel')
            else:
                print('%.1f' %(X/Y))

main()