"""
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

"""
from PyPDF2 import PdfReader

file_path = '../data/input_pdfs/forecasting-05-00009-v2.pdf'

pdf_reader = PdfReader(file_path)


page_count = len(pdf_reader.pages)

page = pdf_reader.pages[1]
text = page.extract_text()


print(f'Total Pages: {page_count}')
print(f'Page 2: {text}')
