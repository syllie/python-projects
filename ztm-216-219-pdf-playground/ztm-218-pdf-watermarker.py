from PyPDF2 import PdfWriter, PdfReader


def add_watermark(input_file, output_file, watermark_file):
    watermark_reader = PdfReader(watermark_file)
    watermark_page = watermark_reader.pages[0]

    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_file, 'wb') as file:
        writer.write(file)


if __name__ == '__main__':
    add_watermark('./pdfs/combined.pdf',
                  './pdfs/combined-watermarked.pdf',
                  './pdfs/wtr.pdf')
