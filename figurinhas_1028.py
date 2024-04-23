from math import gcd

def main() -> None:
    N = int(input())
    for _ in range(N):
        F1, F2 = map(int, input().split())
        pile = gcd(F1, F2)
        print(pile)
        
if __name__ == "__main__":
    main()