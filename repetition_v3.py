#Lista Estrutura de Repeticao TEAMS: PROG III 
#Author: @mthspm
#Exercicios alocados por funcao
#Data: 14/03/2024

import os

class Repetition:
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
        while True:
            value = int(input("Digite um valor entre 0 e 10:"))
            if value >= 0 and value <= 10:
                break
            else:
                continue

    def ex2(self):
        while True:

            user = str(input("Digite um usuario:"))
            pw = str(input("Digite uma senha:"))

            if user == pw:
                print("Cadastro nao pode ser confirmado")
                continue
            else:
                return print("Cadastro realizado com sucesso")
            
    def ex3(self):
        name = str(input("Digite um nome:"))
        age = int(input("Digite uma idade:"))
        salary = float(input("Digite um salario:"))
        sex = str(input("Digite um sexo (f/m):"))
        civil_state = str(input("Digite um estado civil (s/c/v/d):"))

        valid_sexs = ('f', 'm')
        valid_states = ('s', 'c', 'v', 'd')

        if len(name) < 3:
            print("Nome invalido")
        else:
            print("Nome valido")
        if age < 0 or age > 150:
            print("Idade invalida")
        else:
            print("Idade valida")
        if salary <= 0:
            print("Salario invalido")
        else:
            print("Salario valido")
        if sex not in valid_sexs:
            print("Sexualidade invalida")
        else:
            print("Sexualidade valida")
        if civil_state not in valid_states:
            print("Estado civil invalido")
        else:
            print("Estado civil valido")

    def ex4(self):
        pop_a = 80000
        pop_b = 200000

        def raise_tax(pop, percent):
            return pop*percent
        
        while pop_a <= pop_b:
            pop_a += int(raise_tax(pop_a, 0.03))
            pop_b += int(raise_tax(pop_b, 0.015))
            print(f"Populacao em A: {pop_a}")
            print(f"Populacao em B: {pop_b}")
        
        print("Populacao A igualou-se ou superou B")
        print(f"Populacao em A: {pop_a}")
        print(f"Populacao em B: {pop_b}")

    def ex5(self):
        while True:
            pop_a = int(input('Populacao em A: '))
            pop_b = int(input('Populacao em B: '))

            tax_a = int(input('Taxa em A (0-100%): ')) / 100
            tax_b = int(input('Populacao em B (0-100%): ')) / 100

            count = 0

            def raise_tax(pop, percent):
                return pop*percent
            
            while pop_a <= pop_b:
                pop_a += raise_tax(pop_a, tax_a)
                pop_b += raise_tax(pop_b, tax_b)
                print(f"Populacao em A: {pop_a.__round__(0)}")
                print(f"Populacao em B: {pop_b.__round__(0)}")
                count += 1
            
            print(f"Populacao A igualou-se ou superou B em {count} anos")
            print(f"Populacao em A: {pop_a.__round__(0)}")
            print(f"Populacao em B: {pop_b.__round__(0)}")

            repeat = int(input('Digite 1 para repetir, ou qualquer tecla para sair: '))
            if repeat == 1:
                continue
            else:
                return
            
    def ex6(self):
        for i in range(21):
            print(i)

        text = ""
        for i in range(21):
            text += f'{i} '
        print(text)

    def ex7(self):
        a, b, c, d, e = map(int, input("Digite 5 numeros separados na mesma linha: ").split())
        numbers = [a, b, c, d, e]
        numbers.sort(reverse=True)
        print(numbers[0])

    def ex8(self):
        a, b, c, d, e = map(int, input("Digite 5 numeros separados na mesma linha: ").split())
        numbers = [a, b, c, d, e]
        sum = 0
        average = 0
        for n in numbers:
            sum += n

        average = sum / len(numbers)

        print(f"Soma: {sum} | Media: {average}")

    def ex9(self):
        for n in range(51):
            if n % 2 != 0:
                print(n)

    def ex10(self):
        int1 = int(input("Digite um inteiro: "))
        int2 = int(input("Digite outro inteiro: "))
        numbers = []

        if int1 > int2:
            while int1 != int2:
                int2 += 1
                if int2 !=int1:
                    numbers.append(int2)
        elif int1 < int2:
            while int1 != int2:
                int1 += 1
                if int1 != int2:
                    numbers.append(int1)

        print(numbers)

    def ex11(self):
        int1 = int(input("Digite um inteiro: "))
        int2 = int(input("Digite outro inteiro: "))
        numbers = []

        if int1 > int2:
            while int1 != int2:
                int2 += 1
                if int2 !=int1:
                    numbers.append(int2)
        elif int1 < int2:
            while int1 != int2:
                int1 += 1
                if int1 != int2:
                    numbers.append(int1)

        sum = 0
        for n in numbers:
            sum += n

        print(sum)

    def ex12(self):
        entry = int(input("Digite um inteiro para saber sua tabuada: "))
        result = f"Tabuada de {entry}\n"
        for i in range(1,11):
            result += f"{entry} X {i} = {entry*i}\n"

        print(result)

    def ex13(self):
        base = int(input())
        exp = int(input())

        pot = 1

        for count in range(exp):
            pot *= base
            count +=1

        print(base, "^", exp, "=", pot)

    def ex14(self):
        count = {"par": 0,
                 "impar": 0}
        
        for _ in range(10):
            n = int(input("Digite um inteiro: "))
            if n % 2 == 0:
                count["par"] += 1
            else:
                count["impar"] += 1

        print(f"Numeros Primos: {count['impar']}")
        print(f"Numeros Pares: {count['par']}")

    def ex15(self):
        #fibonacci
        #n = n-1 + n-2

        n = int(input("Digite o n-esimo termo da fibonacci"))
        fibo = [1, 1]
        for i in range(n):
            fibo.append(fibo[-1] + fibo[-2])

        print(fibo)

    def ex16(self):
        fibo = [1, 1]
        while True:
            fibo.append(fibo[-1] + fibo[-2])
            if fibo[-1] > 500:
                return print(fibo)
            else:
                continue

    def ex17(self):
        #factorial
        #5! = 5*4*3*2*1
        n = int(input("Digite um numero para saber seu fatorial:"))
        fact = 1

        for i in range(1, n+1):
            fact *= i

        print(fact)

    def ex18(self):
        #conjunto = conjunto de n numeros qualquer que for passada
        entry = input("De um conjunto de numeros separados por espaco na mesma linha").split()
        conjunto = [int(i) for i in entry]

        sum = 0
        for n in conjunto:
            sum += n

        average = sum / len(conjunto)
        conjunto.sort(reverse=True)
        max = conjunto[0]
        min = conjunto[-1]

        print(f"SOMA: {sum}, MEDIA: {average}, MAX: {max}, MIN {min}")

    def ex19(self):
        #conjunto = conjunto de n numeros qualquer que for passada
        while True:
            entry = input("De um conjunto de numeros separados por espaco na mesma linha (0 >= n <= 1000)").split()
            conjunto = [int(i) for i in entry]
            for n in conjunto:
                if n < 0 or n > 1000:
                    print("Somente sao permitidos numeros de 0 a 1000.")
                    conjunto.clear()
                    continue

            break

        sum = 0
        for n in conjunto:
            sum += n

        average = sum / len(conjunto)
        conjunto.sort(reverse=True)
        max = conjunto[0]
        min = conjunto[-1]

        print(f"SOMA: {sum}, MEDIA: {average}, MAX: {max}, MIN {min}")

    def ex20(self):
        while True:
            n = int(input("Digite um numero para saber seu fatorial: (0 <= n < 16)"))
            if n >= 16 or n < 0:
                print("Entrada invalida, somente positivos inteiros menores que 16")
                continue

            fact = 1
            for i in range(1, n+1):
                fact *= i

            print(fact)
            entry = int(input("Digite 1 para recomecar ou qualquer coisa para sair"))
            if entry == 1:
                continue
            else:
                return
            
    def ex21(self):
        integer = int(input("Digite um numero inteiro: "))

        count = 0
        for i in range(1, integer+1):
            if integer % i == 0:
                count += 1
        
        if count == 2:
            print("Primo")
        else:
            print("Nao primo")
            
    def ex22(self):
        integer = int(input("Digite um numero inteiro: "))

        primos = []
        count = 0
        for i in range(1, integer+1):
            if integer % i == 0:
                primos.append(i)
                count += 1
        
        if count == 2:
            print("Primo")
        else:
            print("Nao primo")
            print(f"Divisores: {primos}")
            
    def ex23(self):
        n = int(input("Digite um numero inteiro: "))
        primos = []
        self.calculus_count = 0
        
        # A ideia eh realizar o minimo de calculos possiveis, utilizando as propriedades dos numeros primos para eliminar possibilidades
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True

            if n % 2 == 0 or n % 3 == 0: # Esse trecho elimina muitas possibilidades
                return False
            
            i = 5
            
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0: # Se o numero for divisivel por i ou i+2, entao nao eh primo
                    self.calculus_count += 1 # se o bloco for executado, entao ao menos um calculo foi realizado
                    return False
                
                self.calculus_count += 2 # se a funcao nao retornou aqui, entao duas divisoes foram realizadas
                i += 6 # incremento de 6 para pular os numeros pares e os multiplos de 3, uma vez que ja foram verificados
            return True
        
        for i in range(2, n+1):
            if is_prime(i):
                primos.append(i)
        
        print(f"Foram encontrados {len(primos)} numeros primos")
        print(f"Divisoes realizados: {self.calculus_count}")
        self.calculus_count = 0
        
    def ex24(self):
        notes = list(map(float, input("Insira n notas separadas por espaco: ").split()))
        average = sum(notes) / len(notes)
        print(f"Media: {average}")
        
    def ex25(self):
        people_count = int(input("Digite a quantidade de pessoas: "))
        age_sum = 0
        
        for i in range(people_count):
            age_sum += int(input(f"Digite a idade da pessoa {i+1}: "))
            
        average = age_sum / people_count
        classification = ""
        
        if 0 >= average <= 25:
            classification = "Jovem"
        elif average <= 60:
            classification = "Adulto"
        else:
            classification = "Idoso"
        
        print(f"Media de idade: {round(average)}")
        print(f"Classificacao: {classification}")
        
    def ex26(self):
        politcs = {'joao': 0,
                   'jose': 0,
                   'maria': 0}
        
        voters = int(input("Digite a quantidade de eleitores: "))
        vote_index = 1

        while voters > 0:
            vote = input(f"ELEITOR[{vote_index}] Digite seu voto (Joao, Jose, Maria): ")
            if vote.lower() in politcs:
                politcs[vote] += 1
                voters -= 1
                vote_index += 1
            else:
                print("Voto invalido")
                continue
            
        print(f"Resultado da votacao: {politcs}")
        
    def ex27(self):
        classes = int(input("Digite a quantidade de turmas: "))
        average = 0
        class_index = 1
        
        while classes > 0:
            students = int(input(f"Digite a quantidade de alunos da turma {class_index}: "))
            if students > 40 or students < 0:
                print("Quantidade invalida")
                continue
            average += students
            classes -= 1
            class_index += 1
            
        average /= class_index - 1
        print(f"Media de alunos por turma: {average}")
        
    def ex28(self):
        cds = int(input("Digite a quantidade de CDs comprados: "))
        average = 0
        for cd in range(cds):
            value = float(input(f"Digite o valor do CD {cd+1}: "))
            average += value
            
        average /= cds
        print(f"Media de gasto por CD: {average.__round__(2)}")
        
    def ex29(self):
        products = int(input("Digite a quantidade de produtos: "))
        price = 1.99
        total = 0
        result = "Loja Quase Dois - Tabela de precos\n"
        for i in range(products):
            total += price
            result += f"{i+1} - R$ {total:.2f}\n"
        
        print(result)
        
    def ex30(self):
        price = float(input("Digite o preco do produto: "))
        products = int(input("Digite a quantidade de produtos: "))
        total = 0
        result = f"Preco do pao: {price}\nPanificadora Pao de Ontem - Tabela de precos\n"
        for i in range(products):
            total += price
            result += f"{i+1} - R$ {total:.2f}\n"
        
        print(result)
        
    def ex31(self):
        total = 0
        index = 1
        while True:
            print("Lojas Tabajara")
            while True:
                price = float(input(f"Produto {index} R$: "))
                if price == 0:
                    break
                total += price
                index += 1
            
            print(f"Total: R$ {total}")
            exchange = float(input("Dinheiro: R$ "))
            print(f"Troco: R$ {exchange - total}")
    
    def ex32(self):
        n = int(input("Digite um numero inteiro: "))
        factorial = 1
        result = []
        for i in range(n, 0, -1):
            factorial *= i
            result.append(i)
        
        sequence = " . ".join(map(str, result))
        print(f"{n}! = {sequence} = {factorial}")
        
    def ex33(self):
        data = list(map(float, input("Forneca um conjunto de temperaturas separadas por espaco: ").split()))
        data.sort(reverse=True)
        Max = data[0]
        Min = data[-1]
        average = sum(data) / len(data)
        print(f"Max: {Max:.2f}, Min: {Min:.2f}, Average: {average:.2f}")
        
    def ex34(self):
        #!Exercicio praticamente repetido, mesma logica do ex21
        n = int(input("Digite um numero inteiro: "))
        #check if is prime
        count = 0
        for i in range(2, n):
            if n % i == 0:
                count += 1
            
        if count == 2:
            print("Primo")
        else:
            print("Nao primo")
        
    def ex35(self):
        n = int(input("Digite um numero inteiro: "))
        primos = []
        
        def is_prime(n):
            return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        
        for i in range(1, n+1):
            if is_prime(i):
                primos.append(i)
        
        print(f"Numeros primos: {primos}")
        
    def ex36(self):
        n = int(input("Digite um numero inteiro:"))
        while True:  
            start = int(input("Digite o inicio do intervalo:"))
            end = int(input("Digite o fim do intervalo:"))
            if end < start:
                print("O intervalo final deve ser maior que o inicial!")
                continue
            else:
                break
        
        result = [f"{n} X {i} = {n*i}" for i in range(start, end+1)]
        result = "\n".join(result)
        
        print(f"Tabuada de {n} comecando em {start} e terminando em {end}\n{result}")
        
    #Apartir daqui, acredito que seja melhor separar os exercicios em arquivos diferentes
    #Uma vez que serao necessarios modulos proprios para cada um deles
    
Repetition().navigator()