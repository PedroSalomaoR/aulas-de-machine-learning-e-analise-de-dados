# numpy é um dos pacotes maus úteis para o ramo do aprendizado de máquina e inteligência artificial
#posso usar import numpy as np= cria um apelido para o numpy onde será chama np
import numpy as np

#array = lista, mas todos os elementos devem ser do mesmo tipo
a = np.array([1,2,3])
print(a)

#array com mais de 1 dimensão precisa ter ([()])
#imprime 3 linhas no terminal ,ou seja, uma matriz e a cada , é uma linha a mais
b= np.array([(2,3,4),(5,6,7),(8,9,10)])
print(b)

#gera uma matriz com o numero zero
#estrutura:variavel=np.zeros((Linhas,Colunas))  
c=np.zeros((4,3))
print(c)

#para gerar matriz só de 1 é só usar ones no lugar de zeros
d=np.ones((2,3))
print(d)

#matriz quadrada onde a linha que cruza a matriz da esquerda superior para a direita inferior é composta por numeros 1
e=np.eye(2)
print(e)

#max puxa o maior elementro da matriz, ex:
print(b.max())

#min puxa o menor
print(b.min())

#sum soma os valores da matriz
print(b.sum())

#mean faz a média de todos os elementos da matriz
print(b.mean())

#std mostra o desvio padrão de todos os elementos
print(b.std())
