def bazinga() -> None:
    T = int(input())
    dataset = {
        'tesoura': ['papel', 'lagarto'],
        'papel': ['pedra', 'Spock'],
        'pedra': ['lagarto', 'tesoura'],
        'lagarto': ['Spock', 'papel'],
        'Spock': ['tesoura', 'pedra']
    }
    for i in range(T):
        sheldon_choice, raj_choice = input().split()
        result = ""
        if sheldon_choice == raj_choice:
            result = "De novo!"
        elif raj_choice in dataset[sheldon_choice]:
            result = "Bazinga!"
        else:
            result = "Raj trapaceou!"
        print(f"Caso #{i+1}: {result}")
        
if __name__ == "__main__":
    bazinga()