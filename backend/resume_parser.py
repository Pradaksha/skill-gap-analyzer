from pdfminer.high_level import extract_text

text = extract_text("test_files/sample_resume.pdf")

print("Length:", len(text))
print(text)