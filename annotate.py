import pandas as pd
import time

df = pd.read_csv('tokenized_vocab.csv')

out1 = []
out2 = []
out3 = []
out4 = []

for index, row in df.iterrows():
	print('original: ' + row['original_word'] + 'bert: ' + row['tokenized_by_bert'])

	user_input = int(input('0: good, 1: okay, 2:bad, 3:confused ' ))

	while user_input < 0 or user_input > 3:
		print('try again')
		user_input = input('0: good, 1: okay, 2:bad, 3:confused ' )

	
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

df1 = pd.DataFrame.from_dict(out1, orient="index" )
df2 = pd.DataFrame.from_dict(out2, orient="index" )
df3 = pd.DataFrame.from_dict(out3, orient="index" )
df4 = pd.DataFrame.from_dict(out4, orient="index" )

df1.to_csv('good.csv')
df2.to_csv('okay.csv')
df3.to_csv('bad.csv')
df4.to_csv('confused.csv')







