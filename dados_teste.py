import pandas as pd

rd = pd.read_csv('dados - Página1.csv')
rd = rd.drop(columns=['Maxpulse']) #remove the column 'Maxpulse'
rd = rd.dropna() #removed all NaN
rd['Date'] = rd.loc[26, 'Date'] = '2020/12/26' #change the row 26 to the right format

# a loop to change all the wrong values in 'Duration'
for x in rd.index:
  if rd.loc[x, "Duration"] > 60:
    rd.loc[x, "Duration"] = 60
for x in rd.index:
  if rd.loc[x, "Duration"] < 60:
    rd.loc[x, "Duration"] = 60

print(rd.to_string())
