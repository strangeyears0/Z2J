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

#Extracting multiple pages from a pdf

# from PyPDF2 import PdfFileReader,PdfFileWriter
# from pathlib import Path
#
# pdf_path = (Path.home()/
#             "Pride_and_Prejudice.pdf")
#
# input_pdf = PdfFileReader(str(pdf_path))
#
# pdf_writer = PdfFileWriter()
# for n in range (1,4):
#     page = input_pdf.getPage(n)
#     pdf_writer.addPage(page)
# print(pdf_writer.getNumPages())
#
# with Path("chapter1.pdf").open(mode='wb') as output_file:
#     pdf_writer.write(output_file)
#

# for page in input_pdf.pages[1:4]:
#     pdf_writer.addPage(page)
# with Path("Chapter1_slice.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# exercises1,2,3:
#
#
# from pathlib import Path
# from PyPDF2 import PdfFileReader, PdfFileWriter
#
#
# pdf_path = (Path.home()/  "Pride_and_Prejudice.pdf")
#
#
# pdf_reader = PdfFileReader(str(pdf_path))
#
#
# last_page = pdf_reader.pages[-1]
#
#
# pdf_writer = PdfFileWriter()
# pdf_writer.addPage(last_page)
#
#
# output_path = Path.home() / "last_page.pdf"
# with output_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)
#
# #2
#
# pdf_writer = PdfFileWriter()
# num_pages = pdf_reader.getNumPages()
#
# for idx in range(num_pages):  # NOTE: idx is a common short name for "index"
#     if idx % 2 == 0:  # Check that the index is even
#         page = pdf_reader.getPage(idx)  # Get the page at the index
#         pdf_writer.addPage(page)  # Add the page to `pdf_writer`
#
# output_path = Path.home() / "every_other_page.pdf"
# with output_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)
#
#
#
# #3
#
#
# part1_writer = PdfFileWriter()
# part2_writer = PdfFileWriter()
#
#
# part1_pages = pdf_reader.pages[:150]
# part2_pages = pdf_reader.pages[150:]
#
#
# for page in part1_pages:
#     part1_writer.addPage(page)
#
# for page in part2_pages:
#     part2_writer.addPage(page)
#
#
# part1_output_path = Path.home() / "part_1.pdf"
# with part1_output_path.open(mode="wb") as part1_output_file:
#     part1_writer.write(part1_output_file)
#
# part2_output_path = Path.home() / "part_2.pdf"
# with part2_output_path.open(mode="wb") as part2_output_file:
#     part2_writer.write(part2_output_file)

# 14.3 Challange PDFFILESPLITTER CLASS

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter

class PdfFileSplitter:
    """Class for splitting a pdf into two files."""

    def __init__(self, pdf_path):
        "Open the PDF file with a new PdfFileReader instance"
        self.pdf_reader = PdfFileReader(pdf_path)

        self.writer1 = None
        self.writer2 = None

    def split(self,breakpoint):
        """Split the Pdf Into two PdfFileWriter"""

        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()

        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.addPage(page)
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, filename):
        """Write both PdfFileWriter instance to files"""

        with Path(filename + "_1.pdf").open(mode="wb") as output_file:
            self.writer1.write(output_file)

        with Path(filename + "_2.pdf").open(mode="wb") as output_file:
            self.writer2.write(output_file)


pdf_splitter = PdfFileSplitter("Pride_and_Prejudice.pdf")
pdf_splitter.split(breakpoint=150)
pdf_splitter.write("pride_split")