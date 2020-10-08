nome = str(input("Digite o nome completo: ")).strip()
div = nome.split()
primeiro = div[0]
ultimo = div[len(div)-1]

print("Nome: {}\nPrimeiro nome: {}\nUltimo nome: {}".format(nome,primeiro,ultimo))