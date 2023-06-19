from PIL import Image
import pytesseract

# Path to the PNG file
png_file_path = 'image.png'

# Path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the PNG file and read the text
with Image.open(png_file_path) as img:
    text = pytesseract.image_to_string(img, lang='eng')

# Path to the output file
output_file_path = 'metin.txt'

# Write the text to the output file
with open(output_file_path, mode='w', encoding='utf-8') as file:
    file.write(text)

print('The text in the PNG file has been successfully written to the output file.')
