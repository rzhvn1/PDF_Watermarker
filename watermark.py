import PyPDF2

template = PyPDF2.PdfFileReader(open('pdf-files/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf-files/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('pdf-files/watermarked.pdf', 'wb') as file:
		output.write(file)

