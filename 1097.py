def main():

    I = 1
    J1 = 7
    J2 = 6
    J3 = 5

    while I != 9:

        print('I=%i J=%i' %(I,J1))
        print('I=%i J=%i' %(I,J2))
        print('I=%i J=%i' %(I,J3))

        I += 2
        J1 += 2
        J2 += 2
        J3 += 2

        if I == 9:

            print('I=%i J=%i' %(I,J1))
            print('I=%i J=%i' %(I,J2))
            print('I=%i J=%i' %(I,J3))




main()