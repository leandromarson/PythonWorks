from math import sqrt, floor, ceil
import random

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz quadrada de {} é {:.3f}, floor: {}, ceil: {}'.format(num,raiz,floor(raiz),ceil(raiz)))

rnd = random.random()
rndint = random.randint(1, 100)

print("Random: {}\nRandint: {}".format(rnd,rndint))