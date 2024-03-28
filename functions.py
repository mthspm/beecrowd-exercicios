from datetime import datetime

class Functions:
    def __init__(self):
        pass
   
    def ex1(self):
        n = int(input("Digite um inteiro: "))
        for i in range(1,n+1):
            result = f"{i} " * i
            print(result)
           
    def ex2(self):
        n = int(input("Digite um inteiro: "))
        for i in range(n):
            result = ""
            for j in range(i):
                result += f"{j+1} "
            print(result)
           
    def ex3(self, a, b, c):
        return a+b+c
       
    def ex4(self, arg):
        return "P" if arg > 0 else "N"
       
    def ex5(self):
        def somaImposto(value, imposto):
            return value + value*imposto
           
    def ex6(self):
        while True:
            try:
                print("Conversor de Tempo (digite 'sair' para encerrar)\n")
                hours = int(input("Digite a hora: "))
                mins = int(input("Digite os minutos: "))
            except Exception as e:
                print("Encerrando....")
                break
            meridian = "AM"
            if hours > 12:
                hours -= 12
                meridian = "PM"
            elif hours == 12:
                meridian = "PM"
            elif hours == 0:
                hours = 12
            print (f"{hours:02}:{mins:02} {meridian}")
       
    def ex7(self):
        parcelsOfDay = []
        def ValorPagamento(parcel, latedays):
            if latedays <= 0:
                return parcel
            else:
                return parcel + parcel*0.03 + parcel*0.001*latedays
        while True:
            try:
                print(">>> Registre uma nova parcela! (Digite 'fim' para prosseguir)")
                parcel = float(input("Digite o valor da parcela: "))
                latedays = int(input("Digite o numero de dias atrasads: "))
            except Exception as e:
                print("Encerrando requisicoes...")
                break
           
            newparcel = ValorPagamento(parcel, latedays)
            print(f"Parcela registrada!\n-Valor Inicial: R${parcel}\n-Dias Atrasados {latedays}\n-Novo Valor R${newparcel:.2f}")
            parcelsOfDay.append(f"R${newparcel:.2f}")
           
        print(f"Parcelas registradas no dia: ({len(parcelsOfDay)})")
        print(parcelsOfDay)
        
    def ex8(self):
        n = int(input("Digite um inteiro: "))
        size = len(str(n))
        if n < 0:
            size -= 1
        print(f"Numero de digitos: {size}")
        
    def ex9(self):
        n = int(input("Digite um inteiro: "))

        if n < 0:
            n_abs = abs(n)
            n_reverse = int(str(n_abs)[::-1]) * -1
        else:
            n_reverse = int(str(n)[::-1])
            
        print(f"Número invertido: {n_reverse}")
           

teste = Functions()
teste.ex9()