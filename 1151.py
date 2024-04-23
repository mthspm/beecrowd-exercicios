def fibonacci():
    
    N = int(input())
    a = 0
    b = 1
    
    lista = [a,b]
    resultado = ''
    
    for i in range(N-2):
        
        lista.append(lista[i]+lista[i+1])
        
    for i in lista:
        
        i = '%i ' %i
        resultado += i

        
    resultado = resultado.strip()
    print(resultado)
        
        
    
fibonacci()