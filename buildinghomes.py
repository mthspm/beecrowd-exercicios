## author: mthspm 

def buildinghomes():
    while True:
        a, b, c = map(int, input().split())
        if a == 0:
            break
        
        area = a * b
        lado = (area * 100) // c 
        
        if (area * 100) % c != 0:
            lado += 1
        
        print(lado)

buildinghomes()