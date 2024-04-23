id = int(input())
wt = int(input())
pay_h = float(input())
pay_h = float('%.2f' %pay_h)

salary = wt*pay_h

print('NUMBER = %i' %id)
print('SALARY = U$ %.2f' %salary)