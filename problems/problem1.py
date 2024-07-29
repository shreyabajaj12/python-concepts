from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files=[files for files in os.listdir() if files.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()