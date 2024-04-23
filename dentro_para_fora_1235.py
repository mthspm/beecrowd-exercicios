def main() -> None:
    N = int(input())
    for _ in range(N):
        string = input()
        left_string = string[:len(string)//2]
        right_string = string[len(string)//2:]
        new_string = left_string[::-1] + right_string[::-1]
        print(new_string)
if __name__ == "__main__":
    main()