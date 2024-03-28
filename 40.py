from typing import List

class City:
    def __init__(self, name: str, cars: int, carsAccidents: int):
        self.name = name
        self.cars = cars
        self.carsAccidents = carsAccidents
        
def getCities() -> List[City]:
    MAX_CITIES = 5
    cities = []
    for i in range(MAX_CITIES):
        print("Cidade", i+1)
        name = input("Digite o nome da cidade: ")
        cars = int(input("Digite a quantidade de carros: "))
        carsAccidents = int(input("Digite a quantidade de acidentes com carros: "))
        cities.append(City(name=name, cars=cars, carsAccidents=carsAccidents))
    
    return cities

def getLowestAccidents(cities: List[City]) -> City:
    return min(cities, key=lambda city: city.carsAccidents)

def getHighestAccidents(cities: List[City]) -> City:
    return max(cities, key=lambda city: city.carsAccidents)

def getCarsQuantityAverage(cities: List[City]) -> float:
    return sum(city.cars for city in cities) / len(cities)

def getCarsAccidentsAverage(cities: List[City]) -> float:
    filteredCities = list(filter(lambda city: city.cars < 2000, cities))
    return sum(city.carsAccidents for city in filteredCities) / len(filteredCities)

def printAllData(lowestAccidents: City, highestAccidents: City, carsQuantityAverage: float, carsAccidentsAverage: float):
    print("Cidade com maior indice de acidentes:", highestAccidents.name, highestAccidents.carsAccidents)
    print("Cidade com menor indice de acidentes:", lowestAccidents.name, lowestAccidents.carsAccidents)
    print("Media de carros de todas cidades:", carsQuantityAverage)
    print("Media de acidentes de transito nas cidades com menos de 2000 carros de passeio:", carsAccidentsAverage)
    
def main():
    cities = getCities()
    lowestAccidents = getLowestAccidents(cities)
    highestAccidents = getHighestAccidents(cities)
    carsQuantityAverage = getCarsQuantityAverage(cities)
    carsAccidentsAverage = getCarsAccidentsAverage(cities)
    printAllData(lowestAccidents, highestAccidents, carsQuantityAverage, carsAccidentsAverage)
    
if __name__ == "__main__":
    main()