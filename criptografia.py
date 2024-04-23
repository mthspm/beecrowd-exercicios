def main():
    N = int(input())
    for _ in range(N):
        message = input()
        new_message = ""
        for char in message:
            if char.isalpha():
                new_message += chr(ord(char) + 3)
            else:
                new_message += char
        new_message = new_message[::-1]
        new_message = new_message[:len(new_message) // 2] + "".join([chr(ord(char) - 1) for char in new_message[len(new_message) // 2:]])
        print(new_message)
        
if __name__ == "__main__":
    main()