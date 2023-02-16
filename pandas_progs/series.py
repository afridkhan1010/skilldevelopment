import pandas as pd

mydata=[2,3,6,5,9]
mydata2="afrid khan"
mydata3=[2.0,3,6.5,5,9]
l_data=pd.Series(mydata)
print(l_data)
print(pd.Series(mydata2))
print(pd.Series(mydata3))

l_data_name=pd.Series(mydata,index=["X","Y","Z","X","Y"])
print(l_data_name)
print(l_data_name["X"])

my_data4={"day1":90,"day2":88,"day3":85}
days_data=pd.Series(my_data4)
print(days_data)
particular_days_data=pd.Series(my_data4,index=['day1','day3'])
print(particular_days_data)


#series is like a column and used only for one dimensional data
#data frames are used for multidimensional datas, data sets are more likely to be multidimensional

multi_data={"name":["afrid","tazneen","navshid","sonu"],
            "age":[25,22,22,13]    }
mul_data=pd.DataFrame(multi_data)
print(mul_data)