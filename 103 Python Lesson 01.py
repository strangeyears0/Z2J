from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from pathlib import Path
# pdf_path = (
#     Path.home()/
#     "Pride_and_Prejudice.pdf"
# )
#
# pdf = PdfFileReader(str(pdf_path))
#
# print(pdf.getNumPages())
# print(pdf.documentInfo)
# print(pdf.documentInfo.title)
#
# first_page = pdf.getPage(0)
#
# # print(type(first_page))
#
# # print(first_page.extractText())
#
# for page in pdf.pages:
#     print(page.extractText())

#FROM PDF TO TXT :



# pdf_path = (Path.home()/
#             "Pride_and_Prejudice.pdf")
#
# pdf_reader = PdfFileReader(str(pdf_path))
# output_file_path = Path.home()/"Pride_and_Prejudice.txt"
#
# with output_file_path.open(mode = "w") as output_file:
#     title = pdf_reader.documentInfo.title
#     num_pages = pdf_reader.getNumPages()
#     output_file.write(f"{title} \n Number of pages: {num_pages}")
#     for page in pdf_reader.pages:
#         text = page.extractText()
#         output_file.write(text)
#


# exercises 1,2,3 :
# pdf_path = (Path.home()/
#             "zen.pdf")
#
# pdf_reader = PdfFileReader(str(pdf_path))
#
# print (pdf_reader.numPages)
#
# first_page = pdf_reader.getPage(0)
#
# text = first_page.extractText()
# print(text)

# 14.2 extracting pages from a pdf
# using the pdffilewriter class
# from pathlib import Path

# pdf_writer = PdfFileWriter()
# page = pdf_writer.addBlankPage(width=72,height=72)
# with Path("blank.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)
#
# Extracting a single page from a PDF:

# pdf_path = (Path.home()/
#             "Pride_and_Prejudice.pdf")
# input_pdf = PdfFileReader(str(pdf_path))
#
# first_page = input_pdf.getPage(0)
#
# pdf_writer = PdfFileWriter()
#
# pdf_writer.addPage(first_page)
#
# with Path("first_page.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)