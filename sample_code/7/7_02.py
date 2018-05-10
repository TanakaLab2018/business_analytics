import pandas as pd

d = pd.DataFrame([('Alice',20),('Bob',24)], columns=['Name', 'Age'])
d = pd.DataFrame({'Name':['Alice','Bob'],'Age':[20,24]})


print(d)
