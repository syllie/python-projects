import PyPDF2

with open('./pdfs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)

    page = reader.getPage(0)
    page.rotateCounterClockwise(180)  # rotate is in place

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./pdfs/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

# so - this was the example from the course, using an outdated version of
# PyPDF2. Some of the methods are deprecated - so let's go for a v2
