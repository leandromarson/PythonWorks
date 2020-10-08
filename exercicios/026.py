frase = str(input("Digite uma frase: ")).strip()
min = frase.lower()
a = min.count('a')
a1 = min.find('a')+1
au = min.rfind('a')+1


print("A frase:\n{}\npossui {} letra(s) 'a'\nA primeira letra 'a' aparece na posição {} e a última na posição {}".format(frase,a,a1,au))
