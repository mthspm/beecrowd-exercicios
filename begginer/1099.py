def main():

    N = int(input())

    for i in range(N):

        i = input()

        valores_impares = []
        soma = 0

        i = i.split(" ")

        X,Y = int(i[0]),int(i[1])

        if X < Y:
            A = X
            B = Y
        else:
            A = Y
            B = X

        for n in range(A+1,B):

            if n%2 != 0:
                valores_impares += [n]

        for x in range(len(valores_impares)):
            soma += valores_impares[x]

        print(soma)

main()