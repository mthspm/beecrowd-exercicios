def main() -> None:
    while True:
        try:
            N = int(input())
            matrix = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if i == j:
                        matrix[i][j] = 2
                    if i + j == N - 1:
                        matrix[i][j] = 3
                    if N//3 <= i <= N - N//3 - 1 and N//3 <= j <= N - N//3 - 1:
                        matrix[i][j] = 1
                    if i == j and i + j == N - 1:
                        matrix[i][j] = 4
                        
            for i in range(N):
                for j in range(N):
                    print(matrix[i][j], end='')
                    
                print()
                
            print()
        except EOFError:
            break
        
if __name__ == '__main__':
    main()