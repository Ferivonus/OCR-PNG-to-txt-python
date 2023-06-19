from PIL import Image
import pytesseract
from tkinter import filedialog
import tkinter as tk
import os

# Path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Ask the user to select multiple files
png_file_paths = filedialog.askopenfilenames(title='Select PNG files', filetypes=[('PNG Files', '*.png')])

# Check if files were selected
if png_file_paths:
    for png_file_path in png_file_paths:
        # Open each selected PNG file and read the text
        with Image.open(png_file_path) as img:
            text = pytesseract.image_to_string(img, lang='eng')

        # Create a unique output file path for each selected file
        base_filename = os.path.splitext(os.path.basename(png_file_path))[0]
        output_file_path = base_filename + '.txt'

        # Write the text to the output file
        with open(output_file_path, mode='w', encoding='utf-8') as file:
            file.write(text)

        print(f"The text in {png_file_path} has been successfully written to {output_file_path}.")
else:
    print('No files selected.')
