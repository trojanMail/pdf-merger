#! python
from pypdf import PdfMerger
from sys import argv

# check if input is given
if len(argv) < 2:
    print("usage: python pdfmerger.py file1 file2")
    exit()

# initialize pdf merger
merger = PdfMerger()

# merge pdfs
for pdf in argv:
    merger.append(pdf)

# output pdfs to file
merger.write("merged-pdfs.pdf")

