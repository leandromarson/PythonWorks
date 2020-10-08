nome = str(input("Digite o nome completo:"))

print("Nome em maiúsculo é {}".format(nome.upper()))
print("Nome em minúsculo é {}".format(nome.lower()))
print("Quantidade de letras de nome é {}".format(len(nome) - nome.count(' ')))
dividido = nome.split()
print("Quantidade de letras do primeiro nome ({}) é {}".format(dividido[0],len(dividido[0])))