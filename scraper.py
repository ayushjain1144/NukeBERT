from PIL import Image
import pytesseract
import sys
import tempfile
from pdf2image import convert_from_path

pdf_file = "Pub61517.pdf"

out_file = "out.txt"

out_file_handle = open(out_file, "a")

image_count = 0

with tempfile.TemporaryDirectory() as path:
	images = convert_from_path(pdf_file, output_folder=path, fmt='jpeg')
	print('partial success\n')
	for image in images:

		#image.save('file', 'JPEG')

		image_count = image_count + 1
		text = str(((pytesseract.image_to_string(image))))

		text = text.replace('-\n', '')

		out_file_handle.write(text)

		print('page ' + str(image_count) + ' completed')

out_file_handle.close()