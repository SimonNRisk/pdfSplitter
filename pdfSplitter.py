#imports
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_dir):
    #create output directory if it doesn't exist already
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #read the PDF file
    pdf_reader = PdfReader(input_pdf)

    #loop through all the pages and save them individually
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        #output file name for the individual page (as of now just page_#.pdf)
        output_pdf_path = os.path.join(output_dir, f"page_{page_num + 1}.pdf")
        
        #write the single page to a new PDF file
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"Saved page {page_num + 1} to {output_pdf_path}")

#usage:
input_pdf = "path/to/large/pdf"
output_dir = "path/to/split/pdfs"
split_pdf(input_pdf, output_dir)
