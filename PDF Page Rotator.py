import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

#STEP 1 : Display A File Selection Dialog For Opening a PDF File.

input_path = gui.fileopenbox(
    title="Select a PDF to rotate...",
    default="*pdf"
)

#STEP 2 : If the user cancels the dialog, then exit the program.

if input_path is None:
    exit()

#STEP 3 : Ask the user to select one of 90, 180, 270 degrees.

choices = ("90","180","270")
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation",
    choices=choices,
)
degrees=int(degrees)

#STEP 4 : Display a file selection dialog for saving the rotated PDF.

save_title = "Save the rotated PDF as..."
file_type = "*.pdf"
output_path = gui.filesavebox(title=save_title,default=file_type)

#STEP 5 : If the user tries to save with the same name as the input file:
while input_path == output_path:
    #alert
    gui.msgbox(msg="Cannot overwrite orginal file!")
    #return to step 4
    output_path = gui.filesavebox(title=save_title, default=file_type)

#STEP 6 : If the user cancels the file save dialog then exit the program.

if output_path is None:
    exit()

#STEP 7 : Perform the page rotation

#open selected file:
input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

#rotate all the pages

for page in input_file.pages:
    page = page.rotateClockwise(degrees)
    output_pdf.addPage(page)

#save the rotated pdf to selected file

with open(output_path,"wb") as output_file:
    output_pdf.write(output_file)
