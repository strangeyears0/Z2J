from PyPDF2 import PdfFileReader
from pathlib import Path
pdf_path = (
    Path.home()/
    "Pride_and_Prejudice.pdf"
)

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())
print(pdf.documentInfo)
print(pdf.documentInfo.title)

first_page = pdf.getPage(0)

# print(type(first_page))

# print(first_page.extractText())

for page in pdf.pages:
    print(page.extractText())