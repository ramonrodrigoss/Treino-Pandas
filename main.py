from IPython.display import display
import pandas as pd

#PASSO 1 - Importar a base de dados
tabela = pd.read_csv("telecom_users.csv")

#PASSO 2 - Visualizar a base de dados
#display(tabela)

# PASSO 3 = Tratamento da base de dados
#Colunas Unnamed é inutil - > vamos deletar
tabela = tabela.drop("Unnamed: 0", axis=1)
#Ver se tem coluna que era pra ser um numero e reconhecida com um texo
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")# transforma em numerico, depois se der erro ele vai deixar em branco
#Colunas vazio (NaN)
#1º colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1)
#2º linhas com alguma celula vazias
tabela = tabela.dropna(how="any", axis=0)
#print(tabela.info())

#PASSO 4 - Verificar os clientes que cancelaram
display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #Percentual



