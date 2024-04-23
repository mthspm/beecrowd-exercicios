from typing import Tuple, Generator


def get_input() -> Generator[Tuple[int, int, int, int, int, int], None, None]:
    try:
        while True:
            r1, x1, y1, r2, x2, y2 = map(int, input().split())
            yield r1, x1, y1, r2, x2, y2
    except EOFError:
        return None


def is_inside(r1: int, x1: int, y1: int, r2: int, x2: int, y2: int) -> bool:
    return r1 >= (r2 + ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def main() -> None:
    for r1, x1, y1, r2, x2, y2 in get_input():
        print('RICO' if is_inside(r1, x1, y1, r2, x2, y2) else 'MORTO')


if __name__ == '__main__':
    main()
