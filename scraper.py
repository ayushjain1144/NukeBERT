from PIL import Image
import pytesseract
import sys
import tempfile
from pdf2image import convert_from_path
import os
import PyPDF2




out_file = "out.txt"
out_file_handle = open(out_file, "a")

directory = "Muthu FBR(1)/"
for file in os.listdir(directory):
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

				out_file_handle.write(text)





				
				

				
	print("*************************end******************************")


out_file_handle.close()