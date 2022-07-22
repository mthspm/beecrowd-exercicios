def main():

    resultado = 0
    
    A,N = map(int,input().split())
    
    while True:
        
        if N <= 0:
            N = int(input())
        else:
            break
    
    for i in range(N):
        resultado += A+i
        
    print(resultado)
    
main()