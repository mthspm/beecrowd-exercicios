from typing import Dict

def getDebt() -> float:
    return float(input("Digite o valor da divida: "))

def getFeesDict() -> Dict[int, int]:
    #key=parcelas, value = porcentagem de juros
    return {1: 0, 3: 10, 6: 15, 9: 20, 12: 25}

def incrementDebt(debt: float, juros: int) -> float:
    return debt + (debt * juros / 100)

def showDebtParcels(debt: float, parcels: Dict[int, int]) -> None:
    print("Quantidade de Parcelas | % de Juros | Valor da Parcela")
    for parcel, juros in parcels.items():
        newDebt = incrementDebt(debt, juros)
        print(f"{parcel: <25} {juros: <11} R${newDebt:.2f}")
    
def main():
    parcels = getFeesDict()
    debt = getDebt()
    showDebtParcels(debt, parcels)
    
if __name__ == "__main__":
    main()