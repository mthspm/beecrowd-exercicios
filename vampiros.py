def main() -> None:
    while True:
        EV1, EV2, AT, D = map(int, input().split())
        if EV1 == EV2 == AT == D == 0:
            break
        