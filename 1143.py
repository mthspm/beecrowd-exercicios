def squarecube():

    N = int(input())

    a = 1
    b = 1
    c = 1
    w = 3
    x = 7
    y = 6
    z = 2

    for i in range(N):

        print(a,b,c)

        ###########
        a += 1              # (a) aumenta na taxa de 1 consecutivamente
        ###########
        b += w              # (b) aumenta primeiramente como w=3 e depois sempre este valor + 2
        w += 2
        ###########
        c += x              # (c) aumenta primeiramente como x=7
        x += y*z            #     depois este valor eh sempre somado com (y=6)(z=2) y*z
        z += 1              #     onde z aumenta na taxa de 1 toda vez
        ###########




squarecube()