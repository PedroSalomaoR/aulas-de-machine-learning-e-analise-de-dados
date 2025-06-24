#aula sobre dicionário
#estrutura do dicionário
# dicionario ={'Chave':'valor'}
dicionario = {'Curso':'Python para ML',
              'Produtor':'Didática-tech',
              'Preço':'Gatuito',
              'Nota':'R$300,00'}
#estrutura de pesquisa de valor=print(dicionario['Curso']) e vai retornar o valor da chave 'Curso'
print(dicionario['Curso'])
print(dicionario['Nota'])

#pega um valor do dicionário e o armazena
a=dicionario['Nota']
print(a)

#add chave e valor ao dic
dicionario['Aluno'] = 'Pedro Salomão'
print(dicionario)

#revela as chaves do dic
print(dicionario.keys())

#revela os valores do dic
print(dicionario.values())

#limpa o dic
print(dicionario.clear())