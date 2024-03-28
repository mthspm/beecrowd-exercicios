import re

class Strings:
    def ex1(self):
        str1 = input("String 1: ")
        str2 = input("String 2: ")
        print(f"Tamanho de {str1}: {len(str1)}")
        print(f"Tamanho de {str2}: {len(str2)}")
        print(f"{str1} e {str2} são iguais." if str1 == str2 else f"{str1} e {str2} são diferentes.")
        
    def ex2(self):
        name = input("Digite seu nome: ")
        reversedName = name[::-1]
        def getOnlyUpperLetters(name):
            f = lambda letter: letter.isupper()
            return "".join(filter(f, name))
        reversedNameUpper = getOnlyUpperLetters(reversedName)
        print(reversedNameUpper)
        
    def ex3(self):
        name = input("Digite seu nome: ")
        for letter in name:
            print(letter.upper())
            
    def ex4(self):
        name = input("Digite seu nome: ")
        for i in range(len(name)):
            print(name[:i+1]) # Slicing == Fatiamento de strings por partes
        
    def ex5(self):
        name = input("Digite seu nome: ")
        for i in range(len(name), 0, -1):
            print(name[:i])
            
    def ex6(self):
        date = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        day, month, year = date.split("/")
        calendar = {
            "01": "Janeiro",
            "02": "Fevereiro",
            "03": "Marco",
            "04": "Abril",
            "05": "Maio",
            "06": "Junho",
            "07": "Julho",
            "08": "Agosto",
            "09": "Setembro",
            "10": "Outubro",
            "11": "Novembro",
            "12": "Dezembro"
        }
        print(f"Voce nasceu em {day} de {calendar[month]} de {year}")
        
    def ex7(self):
        vogals = ("a", "e", "i", "o", "u")
        phrase = input("Digite uma frase: ")
        vogals_result = [letter for letter in phrase if letter.lower() in vogals]
        empty_spaces = [letter for letter in phrase if letter == " "]
        print(f"Apareceram {len(vogals_result)} vogais na frase.")
        print(f"Apareceram {len(empty_spaces)} espacos vazios na frase.")
        
    def ex8(self):
        phrase = input("Digite uma frase: ")
        palindrome = phrase.replace(" ", "")
        palindromeReversed = palindrome[::-1]
        result = "é" if palindrome == palindromeReversed else "não é"
        print(f"A frase '{phrase}' {result} um palindromo.")
    
    def ex9(self):
        cpf = input("Digite seu CPF (xxx.xxx.xxx-xx): ")
        
        def validateCPF(cpf):
            #*match() -> busca por padroes em uma expressao regular (regex), retorna None se nao encontrar ou um match obj
            #* \d{3} = espera por 3 digitos, \. = espera por um ponto, - = espera por um hifen
            #*obs: hifen nao precisa de escape por nao ser considerado caractere especial como o ponto.
            if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf) is None:
                return False
            
            numbers = [int(number) for number in cpf if number.isdigit()]
                
            if len(numbers) == 11:
                val1 = False
                val2 = False
                product_sum = sum(a*b for a, b in zip (numbers[0:9], range (10, 1, -1)))
                expected_digit = (product_sum * 10 % 11) % 10
                if expected_digit == numbers[9]:
                    val1 = True
                    
                product_sum = sum(a*b for a, b in zip (numbers[0:10], range (11, 1, -1)))
                expected_digit = (product_sum * 10 % 11) % 10
                if expected_digit == numbers[10]:
                    val2 = True
                
                if val1 and val2:
                    return True
                
            return False
        
        result = "valido" if validateCPF(cpf) else "invalido"
        print(f"O CPF {cpf} é {result}.")
        
    def ex10(self):
        number = int(input("Digite um numero: "))
        units = ("zero", "um", "dois", "tres", "quatro",
                 "cinco", "seis", "sete", "oito", "nove")
        specials = ("dez", "onze", "doze", "treze", "quatorze",
                    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
        tens = ("vinte", "trinta", "quarenta", "cinquenta",
                "sessenta", "setenta", "oitenta", "noventa")
        
        def getExtenseNumber(number):
            if number < 10:
                return units[number]
            elif number < 20:
                return specials[number-10]
            else:
                tens_digit = number // 10
                units_digit = number % 10
                if units_digit == 0:
                    return tens[tens_digit-2]
                else:
                    return f"{tens[tens_digit-2]} e {units[units_digit]}"
                
        print(getExtenseNumber(number))
        
Strings().ex5()