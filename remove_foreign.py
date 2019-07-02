with open("final_data.txt", "r") as f:
	lines = f.readlines()
with open("final_data_new.txt", "w") as f:
	count = 0
	for line in lines:
		try:
			line.encode(encoding='utf-8').decode('ascii')
			f.write(line)
		except UnicodeDecodeError:
			count+=1
			print('caught' + str(count))    
				