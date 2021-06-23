from IPython.display import display
import pandas as pd

#PASSO 1
tabela = pd.read_csv("telecom_users.csv")

#PASSO 2
#display(tabela)

# PASSO 3
#Colunas Unnamed é inutil - > vamos deletar
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
#Ver se tem coluna que era pra ser um numero e reconhecida com um texo

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")# transforma em numerico, depois se der erro ele vai deixar em branco
print(tabela.info())

#Colunas vazio (NaN)
#colunas completamente vazias
#linhas vazias

