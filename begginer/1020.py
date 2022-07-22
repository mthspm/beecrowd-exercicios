idade = int(input())

idade_ano = idade / 365
idade %= 365

idade_mes = idade / 30
idade %= 30

print('%i ano(s)' %idade_ano)
print('%i mes(es)' %idade_mes)
print('%i dia(s)' %idade)

