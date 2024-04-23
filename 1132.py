def main():

    X,Y = int(input()),int(input())

    soma = 0
    A = 0
    B = 0

    if X < Y:
        A = X
        B = Y
    else:
        A = Y
        B = X

    for i in range(A,B+1):

        if i % 13 != 0:

            soma += i

    print(soma)


main()