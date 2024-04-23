def taco():
    
    while True:
        
        N = int(input())
        
        if N >= 1 and N <= 1000:
            break
        
        else:
            continue
    
    total = 0
        
    for i in range(N):
        
        i = input().split()
        
        t1 = int(i[0])
        v1 = int(i[1])
        
        dist1 = v1*t1
        
        total += dist1
        
    return total
        
        
    
a = taco()

print(a)