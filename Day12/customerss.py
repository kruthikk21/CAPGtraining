import pandas as pd

df=pd.read_csv("./Day12/customers-1000.csv")
#df[df.Index<100].to_csv("./Day12/outputcustomers.csv",index=False)
#print(df[df.Index<100].sort_values(by='Index',ascending=False))
#print(df[df.Index<100].groupby('City').sum('Index'))
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe)



