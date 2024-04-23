def cpf():
    while True:
        try:
            cpf = input()
            fragmented_cpf = cpf.split('.')
            fragmented_cpf += fragmented_cpf.pop().split('-')
            for part in fragmented_cpf:
                print(part)
        except EOFError:
            break
        
if __name__ == "__main__":
    cpf()
    
