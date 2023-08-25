from memory_profiler import profile

@profile
def main():
    entry = input()
    entry = list(map(int, entry))

    b1 = 0
    b2 = 0
    for i in range(0,9):
        b1 += entry[i] * (i + 1)  
        b2 += entry[i] * (9 - i)  

    b1 %= 11
    b2 %= 11

    if b1 == 10:
        b1 = 0

    if b2 == 10:
        b2 = 0

    return "{}.{}.{}-{}{}".format(
        "".join(map(str, entry[:3])),
        "".join(map(str, entry[3:6])),
        "".join(map(str, entry[6:9])),
        b1,
        b2
    )

print(main())