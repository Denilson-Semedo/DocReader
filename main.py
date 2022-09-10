import PyPDF2

def main():
    pdfFile = "test.pdf"

    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    page = pdfRead.getPage(0)
    pageContext = page.extractText()
    print(pageContext)



if __name__ == '__main__':
    main()