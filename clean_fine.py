import re

file = 'data.txt'

with open(file, 'r') as f:
	text = f.read()

	re.sub(r'\n\.', '\n', text)
	re.sub(r'\n\s*\n', '\n\n', text)

	with open('out.txt', 'w') as f1:
		f1.write(text)
