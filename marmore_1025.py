def marmore() -> None:
    counter = 1
    while True:
        N, Q = map(int, input().split())
        marmores = []
        if N == Q == 0:
            break
        for _ in range(N):
            marmores.append(int(input()))
            
        for _ in range(Q):
            query = int(input())
            if query in marmores:
                print(f"{query} found at {marmores.index(query) + 2}")
            else:
                print(f"{query} not found")
                
        counter += 1
        
if __name__ == "__main__":
    marmore()