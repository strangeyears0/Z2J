import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

#STEP 1 : Display A File Selection Dialog For Opening a PDF File.

input_path = gui.fileopenbox(
    title="Select a PDF to rotate...",
    default="*pdf"
)