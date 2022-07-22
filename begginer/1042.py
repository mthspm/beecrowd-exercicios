entrada = input()

entrada = entrada.split(" ")

for i in range(len(entrada)):
    entrada[i] = int(entrada[i])

entrada_sorted = sorted(entrada)

print('%i\n%i\n%i\n' %(entrada_sorted[0],entrada_sorted[1],entrada_sorted[2]))

print('%i\n%i\n%i' %(entrada[0],entrada[1],entrada[2]))