real = float(input("Digite quantos R$ tem na carteira: "))
dolar = real/5.29
euro = real/6.29

print("R${:.2f} é igual a US${:.2f} e €{:.2f}".format(real,dolar,euro))