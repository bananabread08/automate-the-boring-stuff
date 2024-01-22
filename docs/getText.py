from docx import Document

# get all strings of a document
def get_text(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

print(get_text('demo.docx'))
