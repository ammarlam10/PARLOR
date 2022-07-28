import pandas as pd


path = '../monthly/post_201903.csv'

df = pd.read_csv(path)

print('With duplicates', df.shape)

df = df.drop_duplicates()

print('no duplicates',df.shape)

df.to_csv(path, index=False)