import easygui as gui
from PyPDF2 import PdfFileWriter,PdfFileReader

# 1 Ask the user to select a PDF file to open.

input_file_path = gui.fileopenbox("","Select a PDf to trim...", "#.pdf")

# 2 If no PDF file is chosen, exit the program

if input_file_path is None:
    exit()
# 3 Ask for a starting page number

page_start = gui.enterbox(
    "Enter the number of the first page to use:","Where to begin?"
)

# 4 If the user don't enter a starting page number, exit

if page_start is None:
    exit()

# 5 Valid page numbers are positive integers. If the user enter an invalid page number:
# - Warn user
# - Return to step 3
input_file = PdfFileReader(input_file_path) #open pdf
total_pages = input_file.getNumPages() # get total num pages
while (
    not page_start.isdigit()
    or page_start == "0"
    or int(page_start) > total_pages
):
    gui.msgbox("Please provide a valid page number.", "Whooops!")
    page_start = gui.enterbox(
        "Enter the number of the first page to use:","Where to begin?"
    )
    if page_start is None:
        exit()
# 6 Ask for an ending page number
page_end = gui.enterbox(
    "Enter the number of last page to use:", "Where to end?"
)
# 7 If the user does not enter and ending page number, exit the program.
if page_end is None:
    exit()
# 8 If the user enters an invalid page number:
# -Warn the user that the entry is invalid
# -Returt to step 6

while(
    not page_end.isdigit()
    or page_end == '0'
    or int(page_end) > total_pages
    or int(page_end) < int(page_start)

):
    gui.msgbox("Please provide a valid page number.","Whooops!")
    page_end = gui.enterbox(
        "Enter the number of the last page to use:", "Where to end?"
    )
    if page_end is None:
        exit()
# 9 Ask for location to save the extract pages
output_file_path = gui.filesavebox("", "Save the trimmed PDF as...","*.pdf")

# 10 If the user does not select save location, exit the program.
if output_file_path is None:
    exit()

# 11 If the chosen save location is the same as the input file path:
# -Warn the user cannot overwrite the input file
# -Return to the step 9
while input_file_path == output_file_path:
    gui.msgbox(
        "Cannot overwrite orginal file!","Please choose another file..."
    )
    output_file_path = gui.filesavebox(
        "","Save the trimmed PDF as....","*.pdf"
    )
    if output_file_path is None:
        exit()
# 12 Perform the page extraction
output_PDF = PdfFileWriter()
for page_num in range(int(page_start) -1,int(page_end)):
    page = input_file.getPage(page_num)
    output_PDF.addPage(page)
with open(output_file_path, "wb") as output_file:
    output_PDF.write(output_file)