#aula de manipulação de string
#selecionando caracteres para imprimir
frase = 'Estou estudando python hoje'
#print(frase[Incio: um char antes do fim])
print(frase[16:22])

#imprimindo de um caracter até o final da frase
print(frase[16:])

#imprimindo do inicio até determinado caracter
print(frase[:22])

#print(frase[Incio: um char antes do fim: numero de caracter por pulo, ou seja, se digitar 1 ele vai de um em um, se digitar 2, de dois em dois])
print(frase[16:22:1])

#contador de caracter
print(frase.count(' '))

#contador de comprimento
print(len(frase))

#subistitui algo por outro:frase.replace('o que vai ser substituido', 'o que vai substituir')
print(frase.replace('hoje', 'agora'))