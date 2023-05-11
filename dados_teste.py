import pandas as pd
import matplotlib

rd = pd.read_csv('dados - Página1.csv')# leio o arquivo
rd = rd.drop(columns=['Maxpulse'])#retiro a coluna 'Maxpulse'
rd = rd.drop(26)#retiro a linha 26
rd = rd.dropna()#retiro todos valores NaN
rd['Date'] = rd['Date'].str.replace('2020/12/', '') #retiro o mês e o ano por serem os mesmo

for x in rd.index: #um looping para que todos valores de 'Duration sejam os mesmos
  if rd.loc[x, "Duration"] > 60:
    rd.loc[x, "Duration"] = 60
for x in rd.index:
  if rd.loc[x, "Duration"] < 60:
    rd.loc[x, "Duration"] = 60

print(rd)
print(rd.plot( 'Date' , 'Calories' ))#crio um grafico
