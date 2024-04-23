def main():

    I = 0
    J1 = 1
    J2 = 2
    J3 = 3

    while True:

        if I == 0  or I == 2:
            print('I=%i J=%i' %(I,J1))
            print('I=%i J=%i' %(I,J2))
            print('I=%i J=%i' %(I,J3))

        elif I == 1:
            print('I=%i J=%i' %(I,2))
            print('I=%i J=%i' %(I,J2))
            print('I=%i J=%i' %(I,J3))
        else:
            print('I=%.1f J=%.1f' %(I,J1))
            print('I=%.1f J=%.1f' %(I,J2))
            print('I=%.1f J=%.1f' %(I,J3))

        I += 0.2
        J1 += 0.2
        J2 += 0.2
        J3 += 0.2

        if I > 1.9:
            print('I=%i J=%i' %(2,J1))
            print('I=%i J=%i' %(2,J2))
            print('I=%i J=%i' %(2,J3))
            break


main()