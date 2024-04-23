def main():
    
    X = int(input())
    Z = int(input())
    soma = X
    total = 1
    
    while True:
        
        if Z < X:
            Z = int(input())
        else:
            break
        
    while soma < Z:
        soma += X + total
        total += 1
            
    print(total)
    
main()