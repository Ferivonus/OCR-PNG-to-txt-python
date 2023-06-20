from PIL import Image
import pytesseract
from tkinter import filedialog, messagebox
import tkinter as tk
import os
import subprocess

# Path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to handle file selection and text extraction
def convert_files():
    # Ask the user to select multiple files
    png_file_paths = filedialog.askopenfilenames(title='Select PNG files', filetypes=[('PNG Files', '*.png')])

    # Check if files were selected
    if png_file_paths:
        # Create a directory to store the text files
        output_directory = 'text_files'
        os.makedirs(output_directory, exist_ok=True)

        for png_file_path in png_file_paths:
            # Open each selected PNG file and read the text
            with Image.open(png_file_path) as img:
                text = pytesseract.image_to_string(img, lang='eng')

            # Create a unique output file path for each selected file
            base_filename = os.path.splitext(os.path.basename(png_file_path))[0]
            output_file_path = os.path.join(output_directory, base_filename + '.txt')

            # Write the text to the output file
            with open(output_file_path, mode='w', encoding='utf-8') as file:
                file.write(text)

            # Open the generated text file using the default text editor
            try:
                subprocess.run(['start', '', output_file_path], check=True, shell=True)
            except Exception as e:
                print(f'Error opening file: {output_file_path}\n{e}')

        # Show a message box indicating the successful conversion
        messagebox.showinfo('Conversion Complete', 'PNG to TXT conversion is complete.')
    else:
        # Show an error message if no files were selected
        messagebox.showerror('No Files Selected', 'No PNG files were selected.')

# Create a Tkinter root window
root = tk.Tk()
root.title('PNG to TXT Converter')

# Set window size and position
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Create a welcome label
welcome_label = tk.Label(root, text='Welcome to PNG to TXT Converter!', font=('Arial', 14))
welcome_label.pack(pady=20)

# Create a button to trigger file selection and conversion
convert_button = tk.Button(root, text='Select PNG Files and Convert', command=convert_files)
convert_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
