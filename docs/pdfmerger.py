from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["meetingminutes1.pdf", "meetingminutes2.pdf"]:
    merger.append(pdf)

merger.write("merged-meeting.pdf")
merger.close()
