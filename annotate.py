import pandas as pd
import time

df = pd.read_csv('tokenized_final.csv')

out1 = []
out2 = []
out3 = []
out4 = []

count = 0
for index, row in df.iterrows():

	try:
		count += 1
		print(str(count) + "	" + 'original: ' + row['original_word'] + 'bert: ' + row['tokenized_by_bert'])

		user_input = input('0: good, 1: okay, 2:bad, 3:confused ' )

		while user_input != '0' and user_input != '1' and user_input != '2' and user_input != '3':
			print('try again')
			user_input = input('0: good, 1: okay, 2:bad, 3:confused ' )
		
		user_input = int(user_input)	

	
		dic = []
		dic.append([row['original_word'], row['tokenized_by_bert']])

		if user_input == 0:
			out1.append(dic)
		elif user_input == 1:
			out2.append(dic)
		elif user_input == 2:
			out3.append(dic)
		else:
			out4.append(dic)
			
		if(count % 2) == 0:
			df1 = pd.DataFrame(out1, columns = ["words"] )
			df2 = pd.DataFrame(out2, columns = ["words"])
			df3 = pd.DataFrame(out3, columns = ["words"])
			df4 = pd.DataFrame(out4, columns = ["words"])
		
			df1.to_csv('good.csv', mode='a', header=False)
			df2.to_csv('okay.csv', mode='a', header=False)
			df3.to_csv('bad.csv', mode='a', header=False)
			df4.to_csv('confused.csv', mode='a', header=False)
			
			out1=[]
			out2=[]
			out3=[]
			out4=[]
			
			print('Checkpoint:' + str(count) +' saved')
			
			
				
	except:
		df1 = pd.DataFrame.from_dict(out1, orient="index" )
		df2 = pd.DataFrame.from_dict(out2, orient="index" )
		df3 = pd.DataFrame.from_dict(out3, orient="index" )
		df4 = pd.DataFrame.from_dict(out4, orient="index" )
		
		df1.to_csv('good.csv')
		df2.to_csv('okay.csv')
		df3.to_csv('bad.csv')
		df4.to_csv('confused.csv')

				

df1 = pd.DataFrame.from_dict(out1, orient="index" )
df2 = pd.DataFrame.from_dict(out2, orient="index" )
df3 = pd.DataFrame.from_dict(out3, orient="index" )
df4 = pd.DataFrame.from_dict(out4, orient="index" )

df1.to_csv('good.csv')
df2.to_csv('okay.csv')
df3.to_csv('bad.csv')
df4.to_csv('confused.csv')







