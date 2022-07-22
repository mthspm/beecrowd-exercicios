def main():
    
    while True:

        X = int(input())

        if X == 0:
            break

        for i in range (X):

            if i == X-1:
                print(i+1, end='\n')

            else:
                print(i+1, end=' ')

main()