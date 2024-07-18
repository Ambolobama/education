import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])
print(one_hot_encoded.head())
#Я не смог сделать это без get_dummies.