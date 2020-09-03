largura = float(input("Largura em metros: "))
altura = float(input("Altura em metros: "))
area = largura * altura
tinta_litros = 2
tinta_necessaria = area/tinta_litros

print("Dimensão: {:.1f}m X {:.1f}m\nÁrea: {:.1f}m^2\nTinta necessária: {:.1f}l".format(largura,altura,area,tinta_necessaria))

