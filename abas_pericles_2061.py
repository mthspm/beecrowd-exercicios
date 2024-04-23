def main() -> None:
    pages, actions = map(int, input().split())
    
    for _ in range(actions):
        action = input()
        
        if action == 'fechou': # +2 pages -1 que foi fechada = +1
            pages += 1
        else:
            pages -= 1
            
    print(pages)
    
if __name__ == "__main__":
    main()