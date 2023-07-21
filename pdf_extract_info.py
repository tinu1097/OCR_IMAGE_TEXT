from PyPDF2 import PdfReader
import docx
from tabulate import tabulate

def extract_data_from_pdf(pdf_path):
    pdf_data = []
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            pdf_data.append([f"Page {page_num + 1}", text.strip()])

    return pdf_data

# def extract_data_from_docx(docx_path):
#     docx_data = []
#     doc = docx.Document(docx_path)

#     for para in doc.paragraphs:
#         docx_data.append(["Paragraph", para.text.strip()])

#     return docx_data

def display_data_in_table(data):
    headers = ["Section", "Text"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)

if __name__ == "__main__":
    pdf_file_path = "/home/teena/Documents/OCR_IMAGE_TEXT/attachments/004_ Pentaho_Mkting_Newsletter_Q2 2017.pdf"
    # docx_file_path = "path/to/your/docx_file.docx"

    pdf_data = extract_data_from_pdf(pdf_file_path)
    # docx_data = extract_data_from_docx(docx_file_path)

    print("PDF Data:")
    display_data_in_table(pdf_data)

    # print("\nDOCX Data:")
    # display_data_in_table(docx_data)
