'''Extracting Text from PDF'''
import fitz


def get_PDF_text(file, outfile_name):
    doc = fitz.open(file)
    outfile = open(outfile_name + '.txt', 'wb')
    for page in doc:
        text = page.get_text("html").encode("utf8")
        outfile.write(text)
        outfile.write(bytes((12,)))
    outfile.close


if __name__ == '__main__':
    get_PDF_text("")

