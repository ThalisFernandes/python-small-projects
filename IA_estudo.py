"""
Código criado usando o Jupyter-lab, Usando as libs seaborn, matplotlib, sklearn e pandas, projeto para previsão de valor para venda de barcos da semana intesivão de python

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

tabela = pd.read_csv(r"C:\Users\thali\Downloads\barcos_ref.csv")

display(tabela)

tabela.corr()[["Preco"]]
y= tabela['Preco']
x= tabela.drop("Preco", axis=1)
X_teste,X_train,Y_teste,Y_train = train_test_split(x, y, test_size=0.3, random_state=1)


arvore_regressao = RandomForestRegressor()
regressao_linear = LinearRegression()


arvore_regressao.fit(X_teste, Y_teste)
regressao_linear.fit(X_teste, Y_teste)

prev_arvore = arvore_regressao.predict(X_train)
prev_regre = regressao_linear.predict(X_train)

print(r2_score(Y_train, prev_arvore))
print(r2_score(Y_train, prev_regre))

tabela_nova = pd.read_csv(r"C:\Users\thali\Downloads\novos_barcos.csv")
display(tabela_nova)

previsao_regre = arvore_regressao.predict(tabela_nova)

print(previsao_regre)
