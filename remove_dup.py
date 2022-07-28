import pandas as pd



df = pd.read_csv('../monthly/post_201903.csv')

print('With duplicates', df.shape)

df = df..drop_duplicates()

print('no duplicates',df.shape)