salario = float(input("Salario em R$: "))
aumento = salario+((salario*15)/100)

print("O salário de R${:.2f} aumentou em 15% que equivale a R${:.2f}".format(salario,aumento))