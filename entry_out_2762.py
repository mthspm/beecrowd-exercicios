def entry():
    while True:
        try:
            inp = input().split('.')
            print(f"{int(inp[1])}.{int(inp[0])}")
        except EOFError:
            break
        
if __name__ == "__main__":
    entry()
    
