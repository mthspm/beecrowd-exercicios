def factorial():
    
    N = int(input())
    
    fact = 1
    
    X = N+1
    
    
    for i in range(1,X-1):
        
        fact *= (N-i)
        
    values = N * fact
        
    
    print(values)


factorial()