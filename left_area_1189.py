def gen_matrix(rows: int, cols: int) -> list[list[float]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def main() -> None:
    S = input()
    matrix = gen_matrix(12, 12)
    for i in range(12):
        for j in range(12):
            matrix[i][j] = float(input())

    Sum = 0

    for i in range(1, 11):
        if i <= 5:
            for j in range(0, i):
                Sum += matrix[i][j]
        else:
            for j in range(0, 11 - i):
                Sum += matrix[i][j]

    if S == "M":
        Sum /= 30

    print(f"{Sum:.1f}")


main()
