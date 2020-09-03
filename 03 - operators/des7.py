largura = float(input("Largura em metros: "))
altura = float(input("Altura em metros: "))
area = largura * altura
tinta_litros = 2
tinta_necessaria = area/tinta_litros

print("Altura: {}m\nLargura: {}m\nÁrea: {}m^2\nTinta necessária: {}l".format(altura,largura,area,tinta_necessaria))

