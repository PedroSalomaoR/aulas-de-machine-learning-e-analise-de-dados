#tupla = lista que não pode ser alterada 
#tuplas ocupam menos memória do que a lista
#algumas coisas que dá para fazer com listas
lista = [2,3,4]
lista[0] = 20
del lista[0]
print(lista)

tupla = (1 , 2 , 3 , 4)
print(tupla[0])

#criando uma nova tupla a partir de uma lista
novatupla=tuple(lista)
print(type(novatupla))

#tuplas com um elemento sem uma vígula o python reconhece apenas um elemento, ou seja, é int
numero = (3)
print(type(numero))
#agora fazendo um elemento com uma vírgula ele reconhece como tupla
numerotupla=(3,)
print(type(numerotupla))
