def validar_senha(s):
    len_s = len(s)
    if len_s < 6 or len_s > 32:
        return 'Senha invalida.'
    
    has_upper = has_lower = has_digit = False
    special_digits = "!'\/|[]`@#$%&*?.,~çáéíóúãõ^{}()=+-_<>:; "

    for char in s:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char in special_digits:
            return 'Senha invalida.'
    
    if not (has_upper and has_lower and has_digit):
        return 'Senha invalida.'

    return 'Senha valida.'

def main():
    while True:
        try:
            senha = input()
            resultado = validar_senha(senha)
            print(resultado)
        except EOFError:
            break
main()
