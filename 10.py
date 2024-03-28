import random
from typing import Tuple

class CrapsGame:
    NATURAL = (7, 11)
    CRAPS = (2, 3, 12)
    POINT = (4, 5, 6, 8, 9, 10)
    GAME_LOSE = 0
    GAME_WIN = 1
    
    def __init__(self) -> None:
        self.turn = 0
        self.game_state = None
        self.first_roll = None
        self.run()
        
    def rollDice(self) -> Tuple[int, int]:
        return random.randint(1,6), random.randint(1,6)
    
    def manageTurn(self, result: int) -> None:
        if not self.turn:
            if result in self.NATURAL:
                self.game_state = self.GAME_WIN
            elif result in self.CRAPS:
                self.game_state = self.GAME_LOSE
            else:
                self.first_roll = result
        else:
            if result == self.first_roll:
                self.game_state = self.GAME_WIN
            elif result == 7:
                self.game_state = self.GAME_LOSE
    
    def nextTurn(self, dice1: int, dice2: int) -> None:
        result = dice1 + dice2
        self.manageTurn(result)
        self.turn += 1
        
    def run(self) -> None:
        print("Bem-vindo ao jogo de Craps!")
        while self.game_state is None:
            dice1, dice2 = self.rollDice()
            self.nextTurn(dice1, dice2)
            print(f"Turno: {self.turn} - Dados: {dice1} e {dice2} - Resultado: {dice1+dice2}")
        print("Fim do Jogo!")
        print("Você ganhou!" if self.game_state == self.GAME_WIN else "Você perdeu!")
        
if __name__ == "__main__":
    CrapsGame()