# using latest version
from pypdf import PdfReader

# read a file and check number of pages
reader = PdfReader('meetingminutes1.pdf')
print(len(reader.pages))

# get a page
page = reader.pages[0]

# extract text
text = page.extract_text()
print(text)

# extract text of all pages
for page_num in range(2):
    print(page_num)
    print(reader.pages[page_num].extract_text())
    print(page_num)
