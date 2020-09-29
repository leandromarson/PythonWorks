from math import hypot

CO = float(input("Comprimento do cateto oposto de um triângulo (m): "))
CA = float(input("Comprimento do cateto adjacente de um triângulo (m): "))
HI = hypot(CO, CA)
print("A hipotenusa equivale a: {:.2f} m".format(HI))