preco = float(input("Insira o preço do produto em R$"))
desconto = (preco*5)/100
total = preco - desconto

print("R${:.2f} com 5% de desconto equivale a: R${:.2f}".format(preco,total))