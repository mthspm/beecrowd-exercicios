#path beecrowd/winter.py
#author: mthspm

def humor(t1,t2,t3):

    if t1 > t2 and t2 <= t3:
        return ":)"
    elif t1 < t2 and t2 >= t3:
        return ":("
    elif t1 < t2 and t2 < t3 and (t3 - t2) < (t2 - t1):
        return ":("
    elif t1 < t2 and t2 < t3 and (t3 - t2) >= (t2 - t1):
        return ":)"
    elif t1 > t2 and t2 > t3 and (t2 - t3) < (t1 - t2):
        return ":)"
    elif t1 > t2 and t2 > t3 and (t2 - t3) >= (t1 - t2):
        return ":("
    elif t1 == t2:
        if t2 < t3:
            return ":)"
        else:
            return ":("
    return ""

def main():

    t1,t2,t3 = map(int,input().split())

    print(humor(t1,t2,t3))

if __name__ == "__main__":
    main()

