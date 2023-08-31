
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, RGBColor
from docx2pdf import convert
import os
import PyPDF2
from PIL import Image


class Results:

    def __init__(self,data):
        self._input_folder = 'file'  # Replace with the path to your input folder
        self._output_pdf = 'file/merged_output.pdf'  # Replace with the desired output PDF filename
        self. _doc_filename = 'file/Ainput.docx'
        self._pdf_filename= 'file/Aoutput.pdf'
        self._data=data
        self.write_to_word()
        # Convert a Word document to a PDF file
        convert(self. _doc_filename, self._pdf_filename)
        # Folder containing PDF and JPG files to merge
        self.merge_pdf_and_image_files()

    def merge_pdf_and_image_files(self):
        pdf_merger = PyPDF2.PdfMerger()
        i = 0
        for filename in os.listdir(self._input_folder):
            if filename.lower().endswith('.pdf') or filename.lower().endswith('.jpg'):
                file_path = os.path.join(self._input_folder, filename)
                if filename.lower().endswith('.pdf'):
                    with open(file_path, 'rb') as pdf_file:
                        pdf_merger.append(pdf_file)
                elif filename.lower().endswith('.jpg'):
                    image = Image.open(file_path)
                    image_pdf = self._input_folder + '/temp_image' + str(i) + '.pdf'
                    image.save(image_pdf, 'PDF')
                    with open(image_pdf, 'rb') as image_pdf:
                        pdf_merger.append(image_pdf)
                    i += 1

        with open(self._output_pdf, 'wb') as output_stream:
            pdf_merger.write(output_stream)

    def write_to_word(self):
        try:
            document = Document()

            for row_data in self._data:
                paragraph = document.add_paragraph(row_data)
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT  # Align to the right

                if 'חשבון חשמל דו-חודשי עמית ועדן' in row_data:
                    # Apply bold formatting to the title
                    run = paragraph.runs[0]
                    run.font.size = Pt(18)
                    run.font.bold = True
                    run.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

                elif 'סה\"כ לתשלום: ' in row_data or 'לתשלום לא יאוחר מתאריך: ' in row_data:
                    # Apply bold formatting to the subtitle
                    run = paragraph.runs[0]
                    run.font.size = Pt(14)
                    run.font.bold = True

                    if 'לתשלום לא יאוחר מתאריך: ' in row_data:
                        run.font.color.rgb = RGBColor(255, 0, 0)  # Red color

                elif '-' * 40 in row_data or '=' * 40 in row_data:
                    # Apply bold formatting to the separators
                    run = paragraph.runs[0]
                    run.font.bold = True

                elif 'נתונים לחישוב' in row_data or 'אפשרויות לתשלום' in row_data:  # Check if the row contains 'ניב קוטק'
                    # Apply underline formatting to the name
                    run = paragraph.runs[0]
                    run.font.underline = True

            document.save(self. _doc_filename)
            print("Data has been written to", self. _doc_filename)
        except Exception as e:
            print("An error occurred:", e)