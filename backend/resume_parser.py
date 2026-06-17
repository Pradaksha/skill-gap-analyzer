import pdfplumber

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_file = "sample_resume.pdf"  # replace with your resume pdf

    extracted_text = extract_text(pdf_file)

    print(extracted_text)