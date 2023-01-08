##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                ##########
####            ####  ####                 ##########
#######          ########                  ##########
#######            ####                    ##########
####             ########                  ##########
####            ####  ####                 ##########
##########     #####  #####     ###     ############### 
##########  #####        #####  ###     ###############

import pandas as pd

informacao = pd.read_csv("D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\owid-energy-data.csv", index_col=0)

print(informacao)

print(informacao.country)

paises_selecionados = informacao.loc[informacao.country.isin(['Italy', 'France', 'Germany', 'United Kingdom'])]

print(paises_selecionados)

paises_selecionados.to_csv(r'D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\paisesescolhidos.csv', index=False)


##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                     #####
####            ####  ####                      #####
#######          ########               #############
#######            ####                 #############
####             ########               #####
####            ####  ####              #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############

import matplotlib.pyplot as plt
import matplotlib.pyplot as mp
import mplcursors
 
plt.close("all")

Italia = paises_selecionados[paises_selecionados.country == "Italy"]
print(Italia.oil_electricity[85:120])

Franca = paises_selecionados[paises_selecionados.country == "France"]
print(Franca)

Alemanha = paises_selecionados[paises_selecionados.country == "Germany"]
print(Alemanha.oil_electricity)

Reino_Unido = paises_selecionados[paises_selecionados.country == "United Kingdom"]
print(Reino_Unido.oil_electricity)

plt.plot(Italia.year, Italia.oil_electricity, marker='o')
plt.plot(Franca.year, Franca.oil_electricity, marker='o')
plt.plot(Alemanha.year, Alemanha.oil_electricity, marker='o')
plt.plot(Reino_Unido.year, Reino_Unido.oil_electricity, marker='o')

plt.title('Evolução da produção de eletricidade nos países')
plt.xlabel('Ano')
plt.ylabel('Produção Eletricidade')
plt.legend(['Italia', 'Frnca', 'Alemanha', 'Reino_Unido'])

plt.show()


##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                     #####
####            ####  ####                      #####
#######          ########                    ########
#######            ####                      ########
####             ########                       #####
####            ####  ####                      #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))

UK_2010 = paises_selecionados.loc[(paises_selecionados.country == "United Kingdom") & (paises_selecionados.year == 2010)]
print(UK_2010)
UK_2010.to_csv(r'D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\UK2010.csv', index=False)
total_produzido = UK_2010.biofuel_electricity + UK_2010.coal_electricity + UK_2010.fossil_electricity + UK_2010.gas_electricity + UK_2010.hydro_electricity + UK_2010.nuclear_electricity + UK_2010.oil_electricity 
print(total_produzido)
labels = ['Biofuel', 'Coal', 'Fossil', 'Gas', 'Hydro', 'Nuclear', 'Oil']
Bio = UK_2010.biofuel_electricity
Coal = UK_2010.coal_electricity
Fossil = UK_2010.fossil_electricity
Gas = UK_2010.gas_electricity
Hydro = UK_2010.hydro_electricity
Nuclear = UK_2010.nuclear_electricity
Oil = UK_2010.oil_electricity
x = np.array([Bio, Coal, Fossil, Gas, Hydro, Nuclear, Oil]).flatten()

plt.pie(x, labels=labels, autopct='%.2f %%')
plt.title('Fontes produção de eletricidade UK 2010')
plt.legend(title = "Tipo Produção")
plt.show()


##########  #####        #####          ####        ####
##########  #####        #####          ####        ####
####           #####  #####             ####        ####  
####            ####  ####              ####        ####
#######          ########               ##################
#######            ####                 ##################
####             ########                           ####
####            ####  ####                          ####
##########     #####  #####     ###                 ####
##########  #####        #####  ###                 ####


Pais = input("Insira o Pais")
print(Pais)


verificar = paises_selecionados.loc[paises_selecionados.country == Pais]
print(verificar)
    
descobrir_ano = verificar.loc[verificar.nuclear_consumption == verificar.nuclear_consumption.max() ]
descobrir_ano.loc[:, ['country','nuclear_consumption', 'year']]
    
    
        
##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####             #####
####            ####  ####              #####
#######          ########               #############
#######            ####                 #############
####             ########                       #####
####            ####  ####                      #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############   

#%matplotlib inline
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

#data = pd.read_csv("C:\Users\duart\Desktop\data\owid-energy-data.csv", index_col=0)

df= pd.read_csv("D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\owid-energy-data.csv", index_col=0)


sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(19.0, 5.5)


#Gráfico de dispersão do consumo de gás vs consumo nuclear
g=sns.scatterplot(x='gas_consumption', y='nuclear_consumption',
                   size='gas_consumption',data=df)
sns.despine()


#Regressão Linear sem intervalo de confiança
sns.regplot(x='gas_consumption', y='nuclear_consumption',
            ci=None, data=df)



###É possível verificar que ao longo do tempo tanto o consumo de gás como o consumo de
###energia nuclear aumentou. Ou seja, há uma tendência/moda entre estes 2, em que
###ambos aumentaram simultaneamente, como é possível verificar através do "declive"
###da reta de regressão linear. Daí os pontos estarem menos dispersos no ínicio onde
###o consumo era 0 em vários países. Com o consequente aumento do consumo nos anos mais
###recentes, os pontos mostram-se mais dispersos.







##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####             #####
####            ####  ####              #####
#######          ########               #############
#######            ####                 #############
####             ########               #####   #####
####            ####  ####              #####   #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############

from sklearn.tree import DecisionTreeRegressor  
import pandas as pd 

informacao = pd.read_csv("D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\owid-energy-data.csv", index_col=0)
print (informacao)
informacao.columns
informacao = informacao.dropna(axis=0)

#Recursos considerados relevantes
recursos = ['year', 'solar_electricity', 'solar_share_elec', 'solar_cons_change_pct','solar_share_energy','solar_cons_change_twh','solar_elec_per_capita','solar_energy_per_capita']
print(recursos)
X = informacao[recursos]
print(X)

#FOCO DE PREVISÃO
y = informacao.solar_consumption
print(y)

#BUILDING MODEL

# Definir o Modelo
_Model = DecisionTreeRegressor(random_state=1)

# Ajustar model
_Model.fit(X, y)

print(X.head())
#EFETUA 5 PREVISOES DAS PRIMEIRAS 5 LINHAS
print("The predictions are")
print(_Model.predict(X.head()))

