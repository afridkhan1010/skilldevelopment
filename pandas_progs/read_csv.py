import pandas as pd
import os

df=pd.read_csv('data.csv')
# print(df.to_string())
print(df)
pd.options.display.max_rows=9999
print(df)
##head() and tail() methods

print(df.head(10))#returns first 10 rows only
print(df.tail(10))#returns last 10 rows only
#if the limit is not defined, the method will return 5 rows only