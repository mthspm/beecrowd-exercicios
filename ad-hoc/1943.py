def topN():
    
    while True:
        
        K = int(input())
        
        if K >= 1 and K <= 100:
            break
        else:
            continue
        
    N = 0
    values = [100,50,25,10,5,3,1]
    
    for i in values:
        
        if K <= i:
            N = i
            
    print('Top %i' %N)
    
    
    
        
topN()