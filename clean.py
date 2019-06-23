import re



def remove_citations(text):
	
	text = re.sub(r'\"[^"]*\"', '', text)
	text =re.sub(r'\([^\(].*\)', '', text)
	text = re.sub(r'et al. ', '', text)

	return text	