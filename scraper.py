from PIL import Image
import pytesseract
import sys
import tempfile
from pdf2image import convert_from_path
import os
import PyPDF2
from string import digits
import spacy
import re

nlp = spacy.load("C:/Users/2017A7PS0093P/Desktop/DATASET/en_vectors_web_lg-2.1.0/en_vectors_web_lg/en_vectors_web_lg-2.1.0")
nlp.add_pipe(nlp.create_pipe('sentencizer'))

#out_file = "out.txt"
#out_file_handle = open(out_file, "a")

out_count = 1

directory = "test_data/"
for file in os.listdir(directory):
	out_file = 'out' + str(out_count)
	out_file_handle = open(out_file, 'w')
	print("************************start*********************************")
	page_count = PyPDF2.PdfFileReader(open(os.path.join(directory, file), 'rb')).getNumPages()
	print(f"Dealing with {page_count} pages!!")
	image_count = 1
	max_limit = 100

	while(image_count <= page_count):
		with tempfile.TemporaryDirectory() as path:
			images = convert_from_path(os.path.join(directory, file), output_folder=path, fmt='jpeg', first_page=image_count, last_page=image_count + 99)
			print('partial success\n')
			
			for image in images:

				print('page ' + str(image_count) + ' started')

				#image.save('file', 'JPEG')

				image_count = image_count + 1
				text = str(((pytesseract.image_to_string(image))))

				text = text.replace('-\n', '')

				#lower case	
				text = text.lower()

				#remove spaces and extra lines and digits
				remove_digits = str.maketrans('', '', digits)
				
				text = "\n".join([(l.strip()).translate(remove_digits) for l in text.splitlines() if l.strip()])
				
				pattern = re.findall(r'[.:\-)(|\\]+', text )

				for match in pattern:
	
					text = text.replace(match, "")
				text.replace('\n', ' ')	

				out_file_handle.write(text)

		out_file_handle.close()

		


				#doc = nlp(text)
				#sentences = doc.sents
				#text = "\n".join(token.string.strip() for token in doc.sents)

			
				

				





				
				

				
	print("*************************end******************************")



	