import pandas as pd

def get_answer_list(answer):

	return [" ".join(s.lower().split()) for s in answer.splitlines() if s.strip()]

def clean_para(para):
	
	return " ".join(para.lower().split())

def find_index(p1, a1):
	
	return [p1.find(a) for a in a1]	

def update_index(para, answers):

	para = [clean_para(p) for p in para]
	answers = [get_answer_list(a) for a in answers]
	ans_list = [find_index(p1, a1) for p1, a1 in zip(para, answers)]
	for index, l in enumerate(ans_list):
		print(index, l)




df = pd.read_csv('qa.csv')
df = df.dropna()
df["index"] = ""


update_index([para for para in df['Paragraph']], [ans for ans in df['Answers']])

"""
answers = df['Answers'][1]
list = get_answer_list(answers)



update_index(para, answers)
"""



	

