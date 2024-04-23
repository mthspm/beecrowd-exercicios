validation = True

while validation is True:
    entrada = input()

    entrada = entrada.split(" ")

    for i in range(len(entrada)):
        entrada[i] = float(entrada[i])

    entrada = sorted(entrada,reverse=True)
    A,B,C = entrada[0],entrada[1],entrada[2]

    if A < 0 or B < 0 or C < 0 :
        validation = True
    else:
        validation = False

classify = []
validation_exist = True

if A >= B+C:
    classify.append("NAO FORMA TRIANGULO")
    validation_exist = False


while validation_exist is True:

    if A**2 == B**2 + C**2:
            classify.append("TRIANGULO RETANGULO")

    if A**2 > B**2 + C**2:
            classify.append("TRIANGULO OBTUSANGULO")

    if A**2 < B**2 + C**2:
            classify.append("TRIANGULO ACUTANGULO")

    if A == B and B == C:
            classify.append("TRIANGULO EQUILATERO")

    if A == B and B != C:
            classify.append("TRIANGULO ISOSCELES")

    if C == B and B != A:
            classify.append("TRIANGULO ISOSCELES")

    validation_exist = False

if len(classify) > 1:
    print(classify[0])
    print(classify[1])

else:
    print(classify[0])
