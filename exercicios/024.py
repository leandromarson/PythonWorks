cidade = str(input("Digite o nome da sua cidade: ")).strip()

div = cidade.split()
title = div[0].title()
se = 'Santo' in title

print("{} começa com a palavra 'Santo'?: {}".format(cidade,se))