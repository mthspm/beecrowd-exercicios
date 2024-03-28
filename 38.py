import time

def main():
    salary = float(input("Enter the salary: "))
    raisePercent = 0.015
    salary += salary*raisePercent
    
    currentYear = time.localtime().tm_year
    for year in range(1997, currentYear+1):
        raisePercent *= 2
        salary += salary*raisePercent
        
    print(f"Salario atual {salary:.2f} reais. Ano atual: {currentYear}.")
    
if __name__ == "__main__":
    main()