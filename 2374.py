def Pneu():
    
    def validInput():
    
        while True:
            
            I = int(input())
            
            if I >= 1 and I <= 40:
                break
            else:
                continue
            
        return I
    
    N = validInput()
    M = validInput()
    
    def difference(a,b):
        
        return (a-b)
    
    return(difference(N,M)) # N = PRESSAO DESEJADA, M = PRESSAO LIDA
    
    
    
p = Pneu()
print(p)