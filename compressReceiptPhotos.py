import os
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader

def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        input_pdf = PdfFileReader(input_file)
        output_pdf = PdfFileWriter()
        
        for i in range(input_pdf.getNumPages()):
            page = input_pdf.getPage(i)
            page.compressContentStreams()
            output_pdf.addPage(page)
            
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)

def choose_file_path():
    file_path = filedialog.askopenfilename(
        title='Select PDF file to compress',
        filetypes=(('PDF files', '*.pdf'), ('All files', '*.*'))
    )
    if file_path:
        input_path_var.set(file_path)

def choose_folder_path():
    folder_path = filedialog.askdirectory(
        title='Select output folder'
    )
    if folder_path:
        output_path_var.set(os.path.join(folder_path, 'compressed.pdf'))

def compress_pdf_gui():
    input_path = input_path_var.get()
    output_path = output_path_var.get()
    compress_pdf(input_path, output_path)
    status_label.config(text=f'Compression complete: {output_path}')

# Create the main window
root = Tk()
root.title('PDF Compressor')

# Create variables to store the input and output file paths
input_path_var = StringVar()
output_path_var = StringVar()

# Create the input file path widget
input_path_label = Label(root, text='Input PDF file:')
input_path_label.grid(row=0, column=0, padx=5, pady=5)
input_path_entry = Entry(root, textvariable=input_path_var)
input_path_entry.grid(row=0, column=1, padx=5, pady=5)
input_path_button = Button(root, text='Browse...', command=choose_file_path)
input_path_button.grid(row=0, column=2, padx=5, pady=5)

# Create the output file path widget
output_path_label = Label(root, text='Output PDF file:')
output_path_label.grid(row=1, column=0, padx=5, pady=5)
output_path_entry = Entry(root, textvariable=output_path_var)
output_path_entry.grid(row=1, column=1, padx=5, pady=5)
output_path_button = Button(root, text='Browse...', command=choose_folder_path)
output_path_button.grid(row=1, column=2, padx=5, pady=5)

# Create the compress button and status label
compress_button = Button(root, text='Compress', command=compress_pdf_gui)
compress_button.grid(row=2, column=1, padx=5, pady=5)
status_label = Label(root, text='')
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start the main event loop
root.mainloop()
