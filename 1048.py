entrada = float(input())
reajuste = 0

if entrada >= 0 and entrada <= 400:
    reajuste = 0.15

elif entrada >= 400.01 and entrada <= 800:
    reajuste = 0.12

elif entrada >= 800.01 and entrada <= 1200:
    reajuste = 0.1

elif entrada >= 1200.01 and entrada <= 2000:
    reajuste = 0.07

else:
    reajuste = 0.04

salary = entrada + entrada*reajuste
reajuste_gain = entrada*reajuste
percent = int(reajuste*100)

print('Novo salario: %.2f' %salary)
print('Reajuste ganho: %.2f' %reajuste_gain)
print('Em percentual:',percent,'%')