import pandas as pd


#ls =['201701','201702','201703','201704',
#'201705','201706','201707','201708',
#'201709','201710','201711','201712',
#'201801','201802','201803','201804',
#'201805','201806','201807','201808',
#'201809','201810','201811','201812']

#ls =['202005','202006','202007','202008','202009','202010','202011','202012']
ls =['202101','202102','202103','202104','202105','202106','202107','202108']

#ls =['201909','201910','201911','201912']


for i in ls:

	path = '../monthly/post_{}.csv'.format(i)

	df = pd.read_csv(path)

	print('With duplicates', df.shape)

	df = df.drop_duplicates()

	print('no duplicates',df.shape)

	df.to_csv(path, index=False)
	print('---------------------------------------')