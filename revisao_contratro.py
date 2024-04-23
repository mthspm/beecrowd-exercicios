def main() -> None:
    while True:
        failed_digit, number = input().split()
        if failed_digit == number == '0': break
        number = number.replace(failed_digit, "")
        print(int(number) if number else 0)
main()