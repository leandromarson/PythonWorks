from math import sin, cos, tan, radians

angulo = float(input("Digite um ângulo qualquer: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O ângulo de {}° possui o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}".format(angulo,seno,cosseno,tangente))