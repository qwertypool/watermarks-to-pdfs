import PyPDF4           #compatible with Python versions 2.6, 2.7, and 3.2 - 3.5. (pip3 install pypdf4)
PyPDF4.PdfFileReader('ipynb.html.pdf')
from PyPDF4 import PdfFileWriter,PdfFileReader

def put_watermark(input_pdf,output_pdf,watermark):
    watermark_instance = PdfFileReader(watermark)   #reads the watermark pdf file through PdfFileReader
    watermark_page = watermark_instance.getPage(0)  #fetches the respective page of watermark(1st page)

    pdf_reader = PdfFileReader(input_pdf)           # Reads the pdf where watermark is to be placed
    pdf_writer = PdfFileWriter()                    #to write the modified pdf with watermarks

    for page in range(pdf_reader.getNumPages()):     #to loop through every page to put watermark
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output_pdf,'wb') as out:
        pdf_writer.write(out)                       #writes to the respective output_pdf provided

if __name__ == "__main__":
    put_watermark(
        input_pdf = 'ipynb.html.pdf',               #the original pdf
        output_pdf = 'watermark_added1.pdf',        #the modified pdf with watermark
        watermark = 'watermark200.pdf'              #the watermark to be provided
    )



