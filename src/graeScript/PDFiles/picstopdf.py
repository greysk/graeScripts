from pathlib import Path

import fitz


def pics2pdf(imgdir: str | Path, outfilename: str = None) -> None:
    # Open new PDF in memory
    doc = fitz.open()

    if isinstance(imgdir, str):
        imgdir = Path(imgdir)

    for img in imgdir.iterdir():
        # open pic as document
        image = fitz.open(img)
        rect = image[0].rect  # pic dimension
        # make a PDF stream
        pdfbytes = image.convert_to_pdf()
        image.close()  # no longer needed

        # open stream as PDF
        imgPdf = fitz.open('pdf', pdfbytes)
        page = doc.new_page(width=rect.width, height=rect.height)

        page.show_pdf_page(rect, imgPdf, 0)  # image fills the page

    if outfilename is None:
        outfilename = imgdir.parts[-1] + '.pdf'
    doc.save(outfilename)


if __name__ == "__main__":
    pass
