def flavious_josephus() -> None:
    nc = int(input()) # number of cases
    for case in range(nc):
        n, k = map(int, input().split()) # n = peoples, k = size of the jump
        ans = 0
        for i in range(1, n+1):
            ans = (ans + k) % i
        print(f"Case {case+1}: {ans+1}")
        
        
if __name__ == "__main__":
    flavious_josephus()