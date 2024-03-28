#Lista Estrutura de Decisao TEAMS: PROG III 
#Author: @mthspm
#Exercicios alocados por funcao
#Data: 29/02/2024

class Decisions:
    def __init__(self) -> None:
        pass
    
    #Funcao para navegar entre os exercicios
    def navigator(self):
        exercicies = len([method for method in dir(self) if method.startswith("ex")])
        while True:
            entry = input(f"Digite o numero do exercicio (1-{exercicies}) (0 para sair): ")
            if entry == "0":
                return print("Saindo...")
            
            for command in dir(self):
                if command == f"ex{entry}":
                    getattr(self, command)()
                    continue

    def ex1(self):
        a, b = map(float, input("Digite dois numeros: ").split())
        if a > b:
            print(a)
        else:
            print(b)
    
    def ex2(self):
        value = float(input("Digite um numero: "))
        if value > 0:
            print("Positivo")
        else:
            print("Negativo")
    
    def ex3(self):
        value = str(input("Digite uma letra (F:Feminino M:Masculino): "))
        if value == "F":
            print("Feminino")
        elif value == "M":
            print("Masculino")
        else:
            print("Sexo invalido")
    
    def ex4(self):
        letter = str(input("Digite uma letra: "))

        vogals = ('a', 'e', 'i', 'o', 'u')
        
        if letter in vogals:
            print("Vogal")
        else:
            print("Consoante")
            
    def ex5(self):
        n1,n2 = map(float, input("Insira duas notas parciais do aluno: ").split())
        average = (n1+n2)/2
        if average == 10:
            print("Aprovado com Distincao")
        elif average >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
    
    def ex6(self):
        n1,n2,n3 = map(float, input("Digite 3 numeros: ").split())
        if n1 > n2 and n1 > n3:
            print(n1)
        elif n2 > n1 and n2 > n3:
            print(n2)
        else:
            print(n3)
    
    def ex7(self):
        n1,n2,n3 = map(float, input("Digite 3 numeros: ").split())
        
        if n1 > n2 and n1 > n3:
            print(n1)
        elif n2 > n1 and n2 > n3:
            print(n2)
        else:
            print(n3)
        
        if n1 < n2 and n1 < n3:
            print(n1)
        elif n2 < n1 and n2 < n3:
            print(n2)
        else:
            print(n3)
            
        #MMAX = max(n1,n2,n3)
        #MMIN = min(n1,n2,n3)
        #print(MMAX, MMIN)
            
    def ex8(self):
        a, b, c = map(float, input("Digite o preco dos produtos: ").split())
        sheepest = min(a,b,c)
        print(sheepest)
        
    def ex9(self):
        a, b, c = map(float, input("Digite 3 numeros: ").split())
        
        if a >= b and a >= c:
            max_number = a
            if b >= c:
                min_number = c
                middle_number = b
            else:
                min_number = b
                middle_number = c
        elif b >= a and b >= c:
            max_number = b
            if a >= c:
                min_number = c
                middle_number = a
            else:
                min_number = a
                middle_number = c
        else:
            max_number = c
            if a >= b:
                min_number = b
                middle_number = a
            else:
                min_number = a
                middle_number = b
        
        print(max_number, middle_number, min_number)
        
        #lista = [a,b,c]
        #lista.sort(reverse=True)
        #print(lista)
        
    def ex10(self):
        turns = {
            "m": "Bom Dia!",
            "v": "Boa Tarde!",
            "n": "Boa Noite!"
        }
        question_txt = f"Ola Aluno! Em que turno voce estuda? Escolha entre as opcoes:\nM-matutino\nV-vespertino\nN-noturno\n"
        
        question = str(input(question_txt))
        
        if question.lower() in turns:
            print(turns[question])
            
        else:
            print("Valor invalido!")
            
    def ex11(self):
        salary = float(input())
        upgrade = 0
        
        if salary <= 280:
            upgrade = 0.2
        elif salary > 280 and salary < 700:
            upgrade = 0.15
        elif salary > 700 and salary < 1500:
            upgrade = 0.1
        else:
            upgrade = 0.05
            
        print(f"Salario antes do reajuste: {salary}")
        print(f"Percentual de aumento: {upgrade*100}%")
        print(f"Valor do aumento: {salary*upgrade}")
        print(f"Novo salario: {salary+(salary*upgrade)}")
        
    def ex12(self):
        hour_price = int(input("Digite o valor da hora trabalhada: "))
        hours = int(input("Digite a quantidade de horas trabalhadas: "))
        
        brute_salary = hour_price * hours
        fgts = 0.11 * brute_salary
        sindicate = 0.03 * brute_salary
        
        ir = 0
        if brute_salary <= 900:
            ir = 0
        elif brute_salary <= 1500:
            ir = 0.05
        elif brute_salary <= 2500:
            ir = 0.1
        else:
            ir = 0.2
            
        ir_value = ir * brute_salary
        liquid_salary = brute_salary - ir_value - sindicate
        
        print(f"Salario Bruto: ({hour_price} * {hours}): R${brute_salary.__round__(2)}")
        print(f"(-) IR ({ir*100}%): R${ir_value.__round__(2)}")
        print(f"(-) Sindicato (3%): R${sindicate.__round__(2)}")
        print(f"FGTS (11%): R${fgts.__round__(2)}")
        print(f"Total de descontos: R${(ir_value+sindicate).__round__(2)}")
        print(f"Salario Liquido: R${liquid_salary.__round__(2)}")
        
    def ex13(self):
        number = int(input("Digite um numero correspondente a um dia da semana (1-7): "))
        week = {
            1: "Domingo",
            2: "Segunda",
            3: "Terca",
            4: "Quarta",
            5: "Quinta",
            6: "Sexta",
            7: "Sabado"
        }
        if number in week:
            print(week[number])
            
        else:
            print("Valor invalido!")
            
    def ex14(self):
        nota1, nota2 = map(float, input("Digite duas notas: ").split())
        average = (nota1+nota2)/2
        concept = ""
        if average > 9 and average <= 10:
            concept = "A"
        elif average > 7.5 and average < 9:
            concept = "B"
        elif average > 6 and average < 7.5:
            concept = "C"
        else:
            concept = "REPROVADO"
        
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Media: {average}")
        print(f"Conceito: {concept}")
        if concept != "REPROVADO":
            print("APROVADO")
            
    def ex15(self):
        a, b, c = map(float, input("Digite 3 lados de um triangulo: ").split())
        
        if a == b and b == c:
            print("Triangulo Equilatero")
        elif a == b or b == c or a == c:
            print("Triangulo Isosceles")
        else:
            print("Triangulo Escaleno")
            
    def ex16(self):
        a, b, c = map(float, input("Bhaskaras Resolver\nDigite os termos a, b, c: ").split())
        
        if a == 0: print("Nao e uma equacao do segundo grau"); return
        
        delta = (b**2) - (4*a*c)
        
        if delta < 0: print("Nao possui raizes reais"); return
        
        x1 = (-b + (delta**0.5))/(2*a)
        x2 = (-b - (delta**0.5))/(2*a)
        
        print(f"Raizes da funcao: x1={x1} e x2={x2}")
            
    def ex17(self):
        year = int(input("Digite um ano: "))
        
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("Ano bissexto")
        else:
            print("Ano nao bissexto")
    
    def ex18(self):
        try:    
            date = input("Digite uma data (dd/mm/aaaa): ")
            day, month, year = map(int, date.split("/"))
        
            rules = {
                1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
            }
            
            if day > rules[month] or day < 1:
                print("Data invalida")
                return

            if month > 12 or month < 1:
                print("Data invalida")
                return
            
            if year < 0:
                print("Data invalida")
                return
            
            print("Data valida")
        except:
            return print("Data invalida")
        
    def ex19(self):    
        number = int(input("Digite um numero: "))
        hundreds = number // 100
        dozens = (number % 100) // 10
        units = (number % 100) % 10
            
        if hundreds > 0:
            print(f"{hundreds} {'centena' if hundreds == 1 else 'centenas'}", end="")
            if dozens > 0 or units > 0:
                print(", ", end="")
                    
        if dozens > 0:
            print(f"{dozens} {'dezena' if dozens == 1 else 'dezenas'}", end="")
            if units > 0:
                print(" e ", end="")
            
        if units > 0:
            print(f"{units} {'unidade' if units == 1 else 'unidades'}", end="")
            
    def ex20(self):
        n1, n2, n3 = map(int, input("Digite 3 notas: ").split())
        average = (n1+n2+n3)/3
        result = ""
        if average == 10:
            result = "Aprovado com Distincao"
        elif average >= 7:
            result = f"Aprovado {average}"
        else:
            result = f"Reprovado {average}"
            
        print(result)
        
    def ex21(self):
        while True:
            withdraw = float(input("Digite o valor do saque: "))
            if withdraw < 10 or withdraw > 600:
                print("Valor invalido")
                continue
            break
        
        notes = [100, 50, 10, 5, 1]
        withdraw_notes = []
        
        for note in notes:
            withdraw_notes.append(withdraw//note)
            withdraw = withdraw % note
        
        for note, qtd in enumerate(withdraw_notes):
            print(f"{int(qtd)} notas de R${notes[note]}")
        
    def ex22(self, n=None):
        #n=none para usar a funcao em outro exercicio
        number = int(input("Digite um numero: ")) if n is None else n
        if number % 2 == 0:
            print("Numero par")
        else:
            print("Numero impar")
    
    def ex23(self, n=None):
        #n=none para usar a funcao em outro exercicio
        entry = float(input("Digite um numero qualquer: ")) if n is None else n
        if entry == round(entry):
            print("Numero inteiro")
        else:
            print("Numero decimal")
            
    def ex24(self):
        a, b = map(float, input("Digite dois numeros: ").split())
        menu = {
            1: "Soma",
            2: "Subtracao",
            3: "Multiplicacao",
            4: "Divisao"
        }
        menu_input = int(input("Escolha uma opcao:\n1-Soma\n2-Subtracao\n3-Multiplicacao\n4-Divisao\n"))
        
        result = 0
        
        def pos_or_neg(number):
            return "Numero Positivo" if number >= 0 else "Numero Negativo"
        
        if menu_input in menu:
            if menu_input == 1:
                result = a+b
            elif menu_input == 2:
                result = a-b
            elif menu_input == 3:
                result = a*b
            else:
                result = a/b
                
            print(f"Resultado: {result}")
            print(pos_or_neg(result))
            self.ex22(result) #chama a funcao ex22 para verificar se o resultado e par ou impar
            self.ex23(result) #chama a funcao ex23 para verificar se o resultado e inteiro ou decimal
            
        else:
            print("Opcao invalida")
            
    def ex25(self):
        questions = ["Telefonou para a vitima?",
                     "Esteve no local do crime?",
                     "Mora perto da vitima?",
                     "Devia para a vitima?",
                     "Ja trabalhou com a vitima?"]
        mesure = 0
        for question in questions:
            answer = input(f"{question} (S/N): ")
            if answer.lower() == "s":
                mesure += 1
        if mesure == 2:
            print("Suspeita")
        elif mesure >= 3 and mesure <= 4:
            print("Cumplice")
        elif mesure == 5:
            print("Assassino")
        else:
            print("Inocente")
            
    def ex26(self):
        liters = float(input("Digite a quantidade de litros: "))
        fuel_type = input("Digite o tipo de combustivel (A:Alcool G:Gasolina): ").upper()
        gas_price = 2.5
        alcohol_price = 1.9
        
        if fuel_type == "A":
            if liters <= 20:
                discount = 0.03
            else:
                discount = 0.05
            total = (liters*alcohol_price) - (liters*alcohol_price*discount)
        elif fuel_type == "G":
            if liters <= 20:
                discount = 0.04
            else:
                discount = 0.06
            total = (liters*gas_price) - (liters*gas_price*discount)
        else:
            print("Valor invalido")
            return
        
        print(f"Valor a ser pago: R${total}")
    
    def ex27(self):
        strawberry = float(input("Digite o 'peso' dos morangos em kg: "))
        apples = float(input("Digite o 'peso' das macas em kg: "))
        
        if strawberry <= 5:
            strawberry_price = 2.5
        else:
            strawberry_price = 2.2
            
        if apples <= 5:
            apples_price = 1.8
        else:
            apples_price = 1.5
            
        total = (strawberry*strawberry_price) + (apples*apples_price)
        
        if (strawberry+apples) > 8 or total > 25:
            total = total * 0.9 #10% de desconto
        
        print(f"Valor a ser pago: R${total.__round__(2)}")
        
    def ex28(self):
        meat_type = input("Digite o tipo de carne\nF:File Duplo\nA:Alcatra\nP:Picanha\n").upper()
        meat_weight = float(input("Digite a quantidade de carne em kg: "))
        
        dataset = {
            "F": (4.9, 5.8),
            "A": (5.9, 6.8),
            "P": (6.9, 7.8)
        }
        
        if meat_type in dataset:
            if meat_weight <= 5:
                total = meat_weight * dataset[meat_type][0]
            else:
                total = meat_weight * dataset[meat_type][1]
                
            meat_type = "File Duplo" if meat_type == "F" else "Alcatra" if meat_type == "A" else "Picanha"
        else:
            print("Tipo de carne invalido")
            return
            
        tabajara_discount = 0.05 * total
        tabajara_card = total - tabajara_discount
        
        print("-"*30)
        print("Cupom Fiscal - Mercado Tabajara")
        output = f"\nTipo de carne: {meat_type}\nPeso: {meat_weight}kg\nTotal a pagar: R${total.__round__(2)}\n"
        output += f"Caso pague no cartao Tabajara: R${tabajara_card.__round__(2)}\nDesconto: R${tabajara_discount.__round__(2)}"
        
        print(output)
        
test = Decisions()
test.navigator()