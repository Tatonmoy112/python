from pypdf import PdfWriter
import os
files=[file for file in os.listdir() if file.endswith(".pdf")]
merger=PdfWriter()
for pdf in files:
    merger.append(pdf)
merger.write("merged_pdf.pdf")
merger.close