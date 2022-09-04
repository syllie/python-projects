from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('./pdfs/dummy.pdf')
writer = PdfWriter()

print(len(reader.pages))

page = reader.pages[0]
writer.add_page(page.rotate(180))

with open('./pdfs/tilt.pdf', 'wb') as file:
    writer.write(file)
