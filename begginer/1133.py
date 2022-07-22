def main():

    A = 0
    B = 0

    X,Y = int(input()), int(input())

    if X < Y:
        A = X
        B = Y

    elif X > Y:
        B = X
        A = Y

    for i in range(A+1,B):

        if i % 5 == 2 or i % 5 == 3:
            print(i)

main()