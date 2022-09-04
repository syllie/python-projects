from PyPDF2 import PdfMerger, PdfWriter
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('./pdfs/combined.pdf')
    merger.close()


if __name__ == '__main__':
    pdf_list = ['./pdfs/dummy.pdf', './pdfs/twopage.pdf', './pdfs/wtr.pdf']
    pdf_combiner(pdf_list)
