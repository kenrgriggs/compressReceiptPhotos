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

def choose_file_paths():
    file_paths = filedialog.askopenfilenames(
        title='Select PDF files to compress',
        filetypes=(('PDF files', '*.pdf'), ('All files', '*.*'))
    )
    if file_paths:
        input_paths_var.set(list(file_paths))

def choose_folder_path():
    folder_path = filedialog.askdirectory(
        title='Select output folder'
    )
    if folder_path:
        output_path_var.set(folder_path)

def compress_pdf_gui():
    input_paths = input_paths_var.get()
    output_path = output_path_var.get()
    
    for input_path in input_paths:
        filename = os.path.splitext(os.path.basename(input_path))[0]
        output_file_path = os.path.join(output_path, f'{filename}_compressed.pdf')
        compress_pdf(input_path, output_file_path)
        
    status_label.config(text=f'Compression complete: {len(input_paths)} files')

# Create the main window
root = Tk()
root.title('PDF Compressor')

# Create variables to store the input and output file paths
input_paths_var = StringVar()
output_path_var = StringVar()

# Create the input file paths widget
input_paths_label = Label(root, text='Input PDF files:')
input_paths_label.grid(row=0, column=0, padx=5, pady=5)
input_paths_listbox = Listbox(root, listvariable=input_paths_var, height=6)
input_paths_listbox.grid(row=0, column=1, padx=5, pady=5)
input_paths_button = Button(root, text='Browse...', command=choose_file_paths)
input_paths_button.grid(row=0, column=2, padx=5, pady=5)

# Create the output file path widget
output_path_label = Label(root, text='Output folder:')
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
