'''Extracting Text from PDF'''
import fitz
from graeScript import outfile_path


def getPDFtext(file, outfile_name):
    doc = fitz.open(file)
    outfile = open(outfile_path() / outfile_name + '.txt', 'wb')
    for page in doc:
        text = page.get_text("html").encode("utf8")
        outfile.write(text)
        outfile.write(bytes((12,)))
    outfile.close
