from pypdf import PdfReader
def extract_text(pdf_path):
    reader=PdfReader(pdf_path)
    all_text=""
    for page in reader.pages:
        text=page.extract_text()
        if text:
            all_text+=text + "\n"
    return all_text
        



    