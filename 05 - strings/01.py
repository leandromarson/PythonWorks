frase = "Curso em Video Python"

print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[:5])# do começo ate o indice 5
print(frase[15:])# de 15 ate o final
print(frase[9:21:2])# de 9 ate 20 pulando de 2 em 2
print(frase[9::3]) # do 9 ate o final pulando de 3 em 3
print(len(frase))
print(frase.count('o')) # quantas vezes aparece a letra o
print(frase.count('o',0,13)) # conta quantas vezes aparece a letra o de 0 a 13
print(frase.find('deo')) # em que indice começa 'deo'
print(frase.find('Android')) # se nao existe na string retorna -1
print('Curso' in frase) # se existe a palavra 'Curso' na frase
print(frase.replace('Python','Android')) # troca Python pra Android
print(frase.upper()) # manda pra maiusculo
print(frase.lower()) # manda pra minusculo
print(frase.capitalize()) # primeira letra maiuscula so
print(frase.title()) # bota maiusculo na primeira letra das palavras
print(frase.strip()) # remove os espaços inuteis
print(frase.rstrip()) # remove os espaços inuteis na direita
print(frase.lstrip()) # remove os espaços inuteis na esquerda
print(frase.split()) # divide todas as palavras com index novo