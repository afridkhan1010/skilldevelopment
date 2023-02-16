import pandas as pd
pd.options.display.max_rows=9999
df=pd.read_csv('data.csv')
print(df.info())

new_df=df.dropna()#this will not change the original data frame, it will remove all the datas frames with null values
# print(new_df.to_string())
new_df.dropna(inplace=True)# this will change the original data frame
# print(new_df)


#fillna()----replaces empty data with vale given

df.fillna(130,inplace=True)
print(df)
#fill values to specified column

df['Calories'].fillna(130,inplace=True)
print(df)

#using mean, median , mode method's values to fill the emppty cells

x=df['Calories'].mean()# the average value
df['Calories'].fillna(x,inplace=True)

y=df['Calories'].median()#  the value in the middle, after you have sorted all values ascending.
df['Calories'].fillna(y,inplace=True)

z=df['Calories'].mode()[0]#   the value that appears most frequently.
df['Calories'].fillna(z,inplace=True)

#changing the data format, bringing back to its right data format
# 22        45           NaN    100       119     282.0
#   23        60  '2020/12/23'    130       101     300.0
#   24        45  '2020/12/24'    105       132     246.0
#   25        60  '2020/12/25'    102       126     334.5
#   26        60      20201226    100       120     250.0
#   27        60  '2020/12/27'     92       118     241.0

df['date']=pd.to_datetime(df['date'])
print(df.to_string())

#removng the rows which are not in correct format
df.dropna(subset=['date'], inplace=True)

#replacing wrong data with right data

df.loc[7,"duration"]=45#this is applicable for small amount of data which can be identified
for x in df.index:
    if df.loc[x,"duration"]>120:
        df.loc[x,"duration"]=45#replacing wrong data with 45
        df.drop(x,inplace=True)#dropping th row completely
        df.drop_duplicates(inplace=True)#deleted duplicates