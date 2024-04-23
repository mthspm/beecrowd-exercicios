def data():
    while True:
        try:
            data = input()
            day, month, year = data.split('/')
            print(f"{month}/{day}/{year}")
            print(f"{year}/{month}/{day}")
            print(f"{day}-{month}-{year}")
        except EOFError:
            break
        
if __name__ == "__main__":
    data()
    
