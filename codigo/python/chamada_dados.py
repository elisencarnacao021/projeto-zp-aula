#Código para ler um arquivo excel usando a biblioteca pandas


import pandas as pd

# efinir o caminho do arquivo excel a ser lido

caminho = "C:\\teste_git_aula\\dados\\não_processados\\tabela_vendas_ZePequeno.xlsx"

# Lendo o arquivo excel usando a função read_excel do pandas e armazenando em um DataFrame

zp = pd.read_excel(caminho)

print(zp) #trás a tabela do excel como um DataFrame do pandas

#Recurso para abrir abas
#zp = pd.read_excel(caminho, sheet_name="nome_da_aba")


print(zp.columns) #mostra as colunas do DataFrame

print(zp.info()) #mostra informações sobre o DataFrame, como número de linhas, colunas, tipos de dados, etc.

print(zp.describe()) #mostra estatísticas descritivas para as colunas numéricas do DataFrame, como média, desvio padrão, valores mínimos e máximos, etc.
