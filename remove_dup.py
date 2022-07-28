import pandas as pd


#ls =['201701','201702','201703','201704',
#'201705','201706','201707','201708',
#'201709','201710','201711','201712',
#'201801','201802','201803','201804',
#'201805','201806','201807','201808',
#'201809','201810','201811','201812']

ls =['201901','201902','201903','201904']


for i in ls:

	path = '../monthly/post_{}.csv'.format(i)

	df = pd.read_csv(path)

	print('With duplicates', df.shape)

	df = df.drop_duplicates()

	print('no duplicates',df.shape)

	df.to_csv(path, index=False)
	print('---------------------------------------')