import utils
import pytesseract
import balloonDetector as detector

folder = '/home/walter/Documents/naruto/Naruto Chapter 0'

paths = utils.takeFilesByExtension(folder, '*.jpg')

pages = detector.detectFromPaths(paths)
text = []
target = 'pt'

for index, page in enumerate(pages):
	result = pytesseract.image_to_string(page)
	print(result)
