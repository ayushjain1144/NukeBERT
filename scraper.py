from PIL import Image
import pytesseract
import sys
import tempfile
from pdf2image import convert_from_path
import os
import PyPDF2
from string import digits
import re
from clean import remove_citations
from gensim.summarization.textcleaner import replace_abbreviations, split_sentences, undo_replacement

out_count = 1
error_count = 0

directory = "1/"
for file in os.listdir(directory):
	out_file = 'out.txt'
	out_file_handle = open(out_file, 'a')
	print("************************start*********************************")
	try:
		page_count = PyPDF2.PdfFileReader(open(os.path.join(directory, file), 'rb')).getNumPages()
	except:
		error_count += 1
		print(error_count)
		continue
	print(f"Dealing with {page_count} pages!!")
	image_count = 1
	max_limit = 100

	#generally last two pages have crap
	while(image_count <= page_count):
		with tempfile.TemporaryDirectory() as path:
			images = convert_from_path(os.path.join(directory, file), output_folder=path, fmt='jpeg', first_page=image_count, last_page=image_count + 99)
			print('partial success\n')
			
			for image in images:

				image_count = image_count + 1
				if image_count > page_count - 2:
					text = ''

				text = str(((pytesseract.image_to_string(image))))

				text = text.replace('-\n', '')

				#last pages tend to have references, which pollute data
				


				text = text.replace('\n', ' ')

				#remove spaces and extra lines and digits
				remove_digits = str.maketrans('', '', digits)

				text = "\n".join([(l.strip()).translate(remove_digits) for l in text.splitlines() if l.strip()])
				
				text = re.sub(r'[.:"\-)(|\\]{2,}', '', text )

				text = remove_citations(text)

				text = replace_abbreviations(text)
				text = split_sentences(text)

				text = '\n'.join([undo_replacement(line) for line in text if len(line.split()) > 5])

				text = text.lower()

				out_file_handle.write(text)

		out_file_handle.write('\n\n')
		out_file_handle.close()
				
	print("*************************end******************************")



	