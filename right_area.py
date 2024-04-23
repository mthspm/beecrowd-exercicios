def gen_matrix(rows: int, cols: int) -> list[list[float]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def main() -> None:
    S = input()
    matrix = gen_matrix(12, 12)
    for i in range(12):
        for j in range(12):
            matrix[i][j] = float(input())

    Sum = 0
    cont = 0
    col = 11
    for i in range(1, 11):
        for j in range(col, 12):
            Sum += matrix[i][j]

            cont += 1
        if i < 5:
            col -= 1
        if i > 5:
            col += 1

    if S == "M":
        Sum /= 30

    print(f"{Sum:.1f}")


main()
