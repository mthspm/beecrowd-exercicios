def sol():
    powers_of_26 = [pow(26, i, 10**9 + 7) for i in range(1004)]

    while True:
        try:
            d = input().strip()
            if d == "":
                break

            place = [ord(c) - 65 for c in d[::-1]]

            ans = sum(place[i] * powers_of_26[i] for i in range(len(place)))

            print(ans % (10**9 + 7))

        except EOFError:
            break

sol()
