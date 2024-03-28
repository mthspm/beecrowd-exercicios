import random
from typing import List, Union
from os import system

class Forca:
    def __init__(self):
        self.setup()
        system('cls')

    def setup(self) -> None:
        self.errors: int = 0
        self.letters: List[str] = []
        self.words: List[str] = self.getWords()
        self.word: str = self.getRandomWord()
        self.stillAlive = lambda: self.errors < 6
        
    def getWords(self) -> List[str]:
        path = 'strings/words.txt'
        with open(path, 'r') as file:
            return file.read().split('\n')
        
    def getRandomWord(self) -> str:
        return random.choice(self.words)
    
    def mutateWord(self) -> None:
        underlines = ' '.join([letter if letter in self.letters else '_' for letter in self.word])
        output = f'A palavra é: {underlines}'
        print(output)
        
    def getLetter(self) -> str:
        while True:
            letter = input('Digite uma letra: ')
            if letter.isalpha() and len(letter) == 1:
                self.letters.append(letter)
                return letter
            print('Digite apenas uma letra!')
            
    def catchErrors(self, letter: str) -> None:
        if letter in self.letters[:-1]:
            print('Você já digitou essa letra!')
            
        elif letter not in self.word:
            self.errors += 1
            print(f"Você errou pela {self.errors}ª vez. Tente de novo!")
            
    def checkWin(self) -> Union[bool, None]:
        word = self.word.replace(' ', '')
        if all([letter in self.letters for letter in word]):
            system('cls')
            print(f'Você venceu!\nA palavra era: {self.word}')
            return True
    
    def play(self):
        while self.stillAlive():
            self.mutateWord()
            letter = self.getLetter()
            self.catchErrors(letter)
            if self.checkWin():
                break
        else:
            system('cls')
            print(f'Você perdeu!\nA palavra era: {self.word}')
        
if __name__ == '__main__':
    forca = Forca()
    forca.play()