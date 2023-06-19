from PIL import Image
import pytesseract
from tkinter import filedialog
import tkinter as tk

# Path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Ask the user to select a file
png_file_path = filedialog.askopenfilename(title='Select PNG file', filetypes=[('PNG Files', '*.png')])

# Check if a file was selected
if png_file_path:
    # Open the selected PNG file and read the text
    with Image.open(png_file_path) as img:
        text = pytesseract.image_to_string(img, lang='eng')

    # Path to the output file
    output_file_path = 'metin.txt'

    # Write the text to the output file
    with open(output_file_path, mode='w', encoding='utf-8') as file:
        file.write(text)

    print('The text in the PNG file has been successfully written to the output file.')
else:
    print('No file selected.')
