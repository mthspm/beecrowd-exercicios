name = str(input())
salary = float(input())
salary = float('%.2f' %salary)
sells = float(input())
sells = float('%.2f' %sells)

total = sells*0.15 + salary

total = float('%.2f' %total)

print('TOTAL = R$ %.2f' %total)