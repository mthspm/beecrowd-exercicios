from typing import Union, List, Dict

class User():
    def __init__(self, height: float, weight: float, id: int) -> None:
        self.height = height
        self.weight = weight
        self.id = id
        
    def __str__(self) -> str:
        return f"Codigo {self.id} - Altura: {self.height}m, Peso: {self.weight}kg"
    
def getUser() -> Union[User, None]:
    print("Ola usuario, por favor, informe seus dados")
    id = int(input("Digite seu codigo pessoal: "))
    height = float(input("Digite sua altura(m): "))
    weight = float(input("Digite seu peso(kg): "))
    if 0 in (height, weight, id):
        return None
    
    return User(height=height, weight=weight, id=id)

def getExtremes(users: List[User]) -> Dict[User]:
    maxHeightUser = max(users, key=lambda user: user.height)
    minHeightUser = min(users, key=lambda user: user.height)
    maxWeightUser = max(users, key=lambda user: user.weight)
    minWeightUser = min(users, key=lambda user: user.weight)
    return {"maxHeight": maxHeightUser, "minHeight": minHeightUser,
            "maxWeight": maxWeightUser, "minWeight": minWeightUser}

def printExtremes(extremes: Dict[User]):
    print("Usuario mais alto: ", extremes["maxHeight"])
    print("Usuario mais baixo: ", extremes["minHeight"])
    print("Usuario mais pesado: ", extremes["maxWeight"])
    print("Usuario mais leve: ", extremes["minWeight"])
    
def run():
    users = []
    while True:
        user = getUser()
        if user is None:
            break
        users.append(user)
        
    extremes = getExtremes(users)
    printExtremes(extremes)

if __name__ == "__main__":
    run()