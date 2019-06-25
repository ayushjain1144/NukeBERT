import re
from gensim.parsing.preprocessing import strip_multiple_whitespaces, strip_short , strip_non_alphanum
from gensim.summarization.textcleaner import undo_replacement




def remove_citations(text):
	
	text = re.sub(r'\"[^"]*\"', '', text)
	text =re.sub(r'\([^\(].*\)', '', text)
	text = re.sub(r'et al. ', '', text)

	return text	

def clean_line(line):
	line = strip_non_alphanum(line)
	line = strip_multiple_whitespaces(line)
	line = strip_short(line)
	line = undo_replacement(line)
	line = line + '.'

	return line	