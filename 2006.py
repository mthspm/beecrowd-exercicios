def cha():
    
    T = int(input())
    
    entrada = input().split()
    
    contador = 0
    
    for i in entrada:
        
        if int(i) == T:
            contador += 1
            
    print(contador)
    
cha()