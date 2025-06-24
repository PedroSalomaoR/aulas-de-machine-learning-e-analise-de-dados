#utilizando a biblioteca pandas para abrir arquivos e precisa do openpyxl
#quando formos estudar o ML, quase sempre vamos abrir com pandas
import pandas as pd

#para abrir arquivos a estrutura é sempre a msm
#estrutura: variavel = pandas.read_excel('caminho')
#obs: lembre de inverter as barras do caminho!
dados = pd.read_excel('C:/Users/User/OneDrive/Documentos/aulas-python/aulas-didatica.tech/pasta-arquivo/arquivo1.xlsx')

#o pandas vai entender que ele pode usar está função pois está variavel é criada no pandas
#vai mostrar a tabela criana no excel
#a coluna da extrema esquerda é o índice, o panda cria isto automaticamente
#com o uso do head ele só exibe 6 linha, se você quiser mais deve colocar o número de linhas que você quer exibe entre ()
print(dados.head())

#por exemplo 
print(dados.head(7))
