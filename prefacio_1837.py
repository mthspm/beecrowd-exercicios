def prefac() -> None:
    a, b = map(int, input().split())
    q = a // b
    r = a % b
    if r < 0:
        r += abs(b)
        q = (a - r) // b
        
    print(q, r)
    
if __name__ == "__main__":
    prefac()