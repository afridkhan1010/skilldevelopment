import pandas as pd

mydataset={"cars":["BMW","Ford","Benz"],
"passengers":[4,7,2]}

mycars=pd.DataFrame(mydataset)
print(mycars)

print(pd.__version__)