def main():
    
    valores = []
    posicao = 0
    maior = 0
    posicao_maior = 0

    for i in range(100):
        posicao += 1
        n = int(input())                                 
        
        if maior < n:
            maior = n
            posicao_maior = posicao
            
    print('%i\n%i' %(maior,posicao_maior))
        

main()