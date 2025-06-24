#tentando abrir arquivos .csv para analise
import pandas as pd

#Planilha baixada da internet
dados = pd.read_csv('C:/Users/User/OneDrive/Documentos/aulas-python/aulas-didatica.tech/pasta-arquivo/athlete_events.csv')

#exibe arquivo no terminal
print(dados.head(5))