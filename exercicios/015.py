dias_aluguel = int(input("Por quantos dias o carro foi alugado?: "))
km_rodado = float(input("Quandos Km o carro rodou?: "))

total = float((dias_aluguel*60)+(km_rodado*0.15))

print("Valor total : R${:.2f}".format(total))