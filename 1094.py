def main():

    N = int(input()) #qnt de casos

    Total = 0
    Tc = 0
    Tr = 0
    Ts = 0

    for i in range(N):

        n = input()

        n = n.split(" ")

        qtd = int(n[0])

        cobaia = str(n[1])

        Total += qtd

        if cobaia == 'C':
            Tc += qtd
        
        elif cobaia == 'R':
            Tr += qtd

        else:
            Ts += qtd

    Pc = (Tc/Total)*100
    a = ('%.2f' %Pc)
    Pr = (Tr/Total)*100
    b = ('%.2f' %Pr)
    Ps = (Ts/Total)*100
    c = ('%.2f' %Ps)
    

    print('Total: %i cobaias\nTotal de coelhos: %i\nTotal de ratos: %i\nTotal de sapos: %i' %(Total,Tc,Tr,Ts))

    print('Percentual de coelhos:',a,'%')
    print('Percentual de ratos:',b,'%')
    print('Percentual de sapos:',c,'%')

main()