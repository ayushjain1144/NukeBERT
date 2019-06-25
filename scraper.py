from PIL import Image
import pytesseract
import sys
import tempfile
from pdf2image import convert_from_path
import os
import PyPDF2
from string import digits
import re
from clean import remove_citations, clean_line
from gensim.summarization.textcleaner import replace_abbreviations, split_sentences, undo_replacement
from gensim.parsing.preprocessing import strip_multiple_whitespaces, strip_short, strip_non_alphanum

out_count = 1
error_count = 0
dir_counter = 0

directory = "test_data/"
for subdir, dirs, files in os.walk(directory):
	out_file = 'test' + str(dir_counter) + '.txt'
	#out_file_handle = open(out_file, 'a', encoding='utf8')


	print('directory: ' + str(dir_counter))

	file_counter = 1
	for file in files:
		print("************************start*********************************")
		print('file: ' + str(file_counter))
		try:
			page_count = PyPDF2.PdfFileReader(open(os.path.join(subdir, file), 'rb')).getNumPages()
		except Exception as e:
			print(str(e))
			error_count += 1
			print(error_count)
			continue
		print(f"Dealing with {page_count} pages!!")
		image_count = 1
		max_limit = 100

		#generally last two pages have crap
		while(image_count <= page_count):
			with tempfile.TemporaryDirectory() as path:
				images = convert_from_path(os.path.join(subdir, file), output_folder=path, fmt='jpeg', first_page=image_count, last_page=image_count + 99)
				print('partial success\n')

				for image in images:

					image_count = image_count + 1
					if image_count > page_count - 2:
						continue

					text = str(((pytesseract.image_to_string(image))))

					text = text.replace('-\n', '')

					#last pages tend to have references, which pollute data



					text = text.replace('\n', ' ')

					#remove spaces and extra lines and digits
					remove_digits = str.maketrans('', '', digits)

					text = "\n".join([(l.strip()).translate(remove_digits) for l in text.splitlines() if l.strip()])

					text = re.sub(r'[.:"\-)\[\](|\\]{2,}', '', text )
					text = re.sub(r'[+\-*/~%]', '', text)

					text = remove_citations(text)

					text = replace_abbreviations(text)
					text = split_sentences(text)
					

					



					text = '\n'.join([clean_line(line) for line in text if len(line.split()) > 5])

					text = text.lower()
					text = text + '\n'
					
					try:
						with open(out_file, 'a') as out_file_handle:
							out_file_handle.write(text)
							#print(image_count)
					except UnicodeEncodeError:
						print(image_count)
						image_count = page_count + 1
						continue
					except Exception as e:
						print(str(e))
						print(image_count)
						print('no idea')
						image_count = page_count + 1
						continue

					

						

		#out_file_handle.write('\n\n')
					
					
		
		file_counter += 1
		print("*************************end******************************")

	
	dir_counter += 1


	print('***************end directory************************')