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

# from pathlib import Path
#
# from PyPDF2 import PdfFileReader, PdfFileWriter
#
# class PdfFileSplitter:
#     """Class for splitting a pdf into two files."""
#
#     def __init__(self, pdf_path):
#         "Open the PDF file with a new PdfFileReader instance"
#         self.pdf_reader = PdfFileReader(pdf_path)
#
#         self.writer1 = None
#         self.writer2 = None
#
#     def split(self,breakpoint):
#         """Split the Pdf Into two PdfFileWriter"""
#
#         self.writer1 = PdfFileWriter()
#         self.writer2 = PdfFileWriter()
#
#         for page in self.pdf_reader.pages[:breakpoint]:
#             self.writer1.addPage(page)
#         for page in self.pdf_reader.pages[breakpoint:]:
#             self.writer2.addPage(page)
#
#     def write(self, filename):
#         """Write both PdfFileWriter instance to files"""
#
#         with Path(filename + "_1.pdf").open(mode="wb") as output_file:
#             self.writer1.write(output_file)
#
#         with Path(filename + "_2.pdf").open(mode="wb") as output_file:
#             self.writer2.write(output_file)
#
#
# pdf_splitter = PdfFileSplitter("Pride_and_Prejudice.pdf")
# pdf_splitter.split(breakpoint=150)
# pdf_splitter.write("pride_split")


# 14.4 Concatenanting and Merging PDFs

# from PyPDF2 import PdfFileMerger
# from pathlib import Path
# reports_dir = (Path.home()/
#             "Expense_reports"
#                 )
#
# pdf_merger = PdfFileMerger()
# for path in reports_dir.glob("*.pdf"):
#     print(path.name)
# expense_reports = list(reports_dir.glob("*.pdf"))
# expense_reports.sort()
#
# for path in expense_reports:
#     print(path.name)
#
# for path in expense_reports:
#     pdf_merger.append(str(path))
# with Path("expense_reports.pdf").open(mode = "wb") as output_file:
#     pdf_merger.write(output_file)

# exercise1

#
# from pathlib import Path
#
#
# from PyPDF2 import PdfFileMerger
#
# BASE_BATH = Path.home()/ "practice_files"
#
# pdf_paths= [BASE_BATH/"merge1.pdf", BASE_BATH / "merge2.pdf"]
# pdf_merger = PdfFileMerger()
#
# for path in pdf_paths:
#     pdf_merger.append(str(path))
#
# output_path = Path.home() / "concatenated.pdf"
# with output_path.open(mode="wb") as output_file:
#     pdf_merger.write(output_file)
#
# #
# # exercise2
# pdf_merger = PdfFileMerger()
# pdf_merger.append(str(output_path))
#
# pdf_path = BASE_BATH / "merge3.pdf"
# pdf_merger.merge(1,str(pdf_path))
#
# output_path = Path.home() / "merged.pdf"
# with output_path.open(mode = "wb") as output_file:
#     pdf_merger.write(output_file)
#
# from pathlib import Path
# from PyPDF2 import PdfFileReader,PdfFileWriter
#
# pdf_path = Path.home() / "ugly.pdf"
#
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
#
# for n in range(pdf_reader.getNumPages()):
#     page = pdf_reader.getPage(n)
#     if n % 2 == 0:
#         page.rotateClockwise(90)
#     pdf_writer.addPage(page)
#
# with Path("ugly_rotated.pdf").open(mode = "wb") as output_file:
#     pdf_writer.write(output_file)
#
# page=pdf_reader.getPage(0)
# print(page["/Rotate"])
# page.rotateClockwise(90)
# print(page["/Rotate"])

# Cropping Pages
#
# from pathlib import Path
# from PyPDF2 import PdfFileReader,PdfFileWriter
#
# pdf_path= (
#     Path.home()/"half_and_half.pdf"
# )
#
# pdf_reader = PdfFileReader(str(pdf_path))
# first_page = pdf_reader.getPage(0)
#
# print(first_page.mediaBox)
# print(first_page.mediaBox.lowerLeft)
# print(first_page.mediaBox.lowerRight)
# print(first_page.mediaBox.upperLeft)
# print(first_page.mediaBox.upperRight)
# print(first_page.mediaBox.upperRight[0])
# print(first_page.mediaBox.upperRight[1])
# first_page.mediaBox.upperLeft=(0,480)
# print(first_page.mediaBox.upperLeft)
# print(first_page.mediaBox.upperRight)
#
# pdf_writer = PdfFileWriter()
# pdf_writer.addPage(first_page)
# with Path("cropped_page.pdf").open(mode= "wb") as output_file:
#     pdf_writer.write(output_file)
#
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
#
# first_page =  pdf_reader.getPage(0)
#
# import copy
# left_side = copy.deepcopy(first_page)
#
# current_coords = left_side.mediaBox.upperRight
#
# new_coords = (current_coords[0]/2,current_coords[1])
#
# left_side.mediaBox.upperRight = new_coords
#
# right_side=  copy.deepcopy(first_page)
# right_side.mediaBox.upperLeft = new_coords
#
# pdf_writer.addPage(left_side)
# pdf_writer.addPage(right_side)
#
# with Path("cropped_pages.pdf").open(mode="wb") as output_file:
#     pdf_writer.write(output_file)



# ex1

# from pathlib import Path
#
# from PyPDF2 import PdfFileWriter,PdfFileReader
#
# pdf_path = (Path.home()/
#             "split_and_rotate.pdf")
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
#
# for page in pdf_reader.pages:
#     rotated_page = page.rotateCounterClockwise(90)
#     pdf_writer.addPage(rotated_page)
#
# output_path = Path.home() / "rotated.pdf"
# with output_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# ex2
# import copy
#
# pdf_path = Path.home()/"rotated.pdf"
#
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
#
# for page in pdf_reader.pages:
#     upper_right_coords = page.mediaBox.upperRight
#     center_coords = (upper_right_coords[0] / 2, upper_right_coords[1])
#
#     left_page = copy.deepcopy(page)
#     right_page = copy.deepcopy(page)
#
#     left_page.mediaBox.upperRight = center_coords
#     right_page.mediaBox.upperLeft = center_coords
#
#     pdf_writer.addPage(left_page)
#     pdf_writer.addPage(right_page)
#
# output_path = Path.home() / "split.pdf"
#
# with output_path.open(mode = "wb") as output_file:
#     pdf_writer.write(output_file)

# 14.6 Encrypting and Decrypying pdfs
#
# from pathlib import Path
# from PyPDF2 import PdfFileReader,PdfFileWriter
#
# pdf_path = (Path.home()/"newsletter.pdf")
#
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
# pdf_writer.appendPagesFromReader(pdf_reader)
#
# pdf_writer.encrypt(user_password="SuperSecret")
#
# output_path = Path.home()/"newsletter_protected.pdf"
# with output_path.open(mode="wb") as output_file:
#     pdf_writer.write(output_file)

# from pathlib import Path
# from PyPDF2 import PdfFileWriter, PdfFileReader
#
# pdf_path = Path.home() / "newsletter_protected.pdf"
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_reader.decrypt(password="SuperSecret")
# print(pdf_reader.getPage(0))

# ex1

# from pathlib import Path
# from PyPDF2 import PdfFileReader, PdfFileWriter
#
# pdf_path = Path.home()/"top_secret.pdf"
# pdf_reader= PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
# pdf_writer.appendPagesFromReader(pdf_reader)
# pdf_writer.encrypt(user_password="Unguessable")
#
# output_path = Path.home()/"top_secret_encrypted.pdf"
# with output_path.open(mode = "wb") as output_file:
#     pdf_writer.write(output_file)

# ex2
#
# pdf_path = Path.home() / "top_secret_encrypted.pdf"
# pdf_reader = PdfFileReader(str(pdf_path))
#
# pdf_reader.decrypt("Unguessable")
#
# first_page = pdf_reader.getPage(0)
# print(first_page.extractText())

# 14.7 Challenge Unscramble a PDF
#
# from pathlib import Path
# from PyPDF2 import PdfFileReader, PdfFileWriter
#
# def get_page_text(page):
#     return page.extractText()
#
# pdf_path = Path.home()/"scrambled.pdf"
#
# pdf_reader = PdfFileReader(str(pdf_path))
# pdf_writer = PdfFileWriter()
#
# pages = list(pdf_reader.pages)
# pages.sort(key=get_page_text)
#
# for page in pages:
#     rotation_degrees = page["/Rotate"]
#     if rotation_degrees != 0:
#         page.rotateCounterClockwise(rotation_degrees)
#     pdf_writer.addPage(page)
# output_path = Path.home()/"unscrambled.pdf"
# with output_path.open(mode = "wb") as output_file:
#     pdf_writer.write(output_file)

# 14.8 CREATING PDF FROM SCRATCH

# from reportlab.pdfgen.canvas import Canvas
# from reportlab.lib.units import inch,cm
# from reportlab.lib.pagesizes import LETTER
#
#
# # canvas = Canvas("hello.pdf")
# # canvas = Canvas('hello.pdf',pagesize=LETTER)
# # canvas.drawString(72,72,"Hello, World")
# # canvas.save()
# #
# canvas = Canvas("font-example.pdf",pagesize=LETTER)
# canvas.setFont("Times-Roman",18)
# canvas.drawString(1*inch,10*inch,"Times New Roman (18pt)")
# canvas.save()

# from reportlab.lib.colors import blue
# from reportlab.lib.pagesizes import LETTER
# from reportlab.lib.units import inch
# from reportlab.pdfgen.canvas import Canvas
#
# canvas = Canvas("font-colors.pdf", pagesize = LETTER)
#
# canvas.setFont("Times-Roman",42)
#
# canvas.setFillColor("blue")
# canvas.drawString(1*inch,10*inch,"Blue Text")
# canvas.save()