from pathlib import Path

import PyPDF2


def create_new(pdf_writer, output_file: Path) -> None:
    with open(output_file, 'wb') as f:
        pdf_writer.write(f)


def extract_page_from_pdf(pdf_file: str, page_number: int) -> None:
    pdf_writer = PyPDF2.PdfFileWriter()
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        page_obj = pdf_reader.getPage(page_number)
    pdf_writer.addPage(page_obj)
    output_file = Path(pdf_file).with_stem(
        Path(pdf_file).stem + f'_pg{page_number}.pdf')
    create_new(pdf_writer, output_file)


def copy_pdf(pdf_file: str) -> None:
    pdf_writer = PyPDF2.PdfFileWriter()
    output_file = Path(pdf_file).with_stem(
            Path(pdf_file).stem + '_copy.pdf')
    with open(pdf_file, 'rb') as f, open(output_file, 'wb') as o:
        pdf_reader = PyPDF2.PdfFileReader(f)
        page_numbers = pdf_reader.getNumPages()
        for page_num in range(page_numbers):
            page_obj = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)
        pdf_writer.write(o)


def rotate_right(pdf_file: str, degrees: int, page_num: int = 0) -> None:
    pdf_writer = PyPDF2.PdfFileWriter()
    output_file = Path(pdf_file).with_stem(
            Path(pdf_file).stem + f'_{page_num}rotated{degrees}')
    print(f'Rotating file {degrees} degrees.')
    with open(pdf_file, 'rb') as f, open(output_file, 'wb') as o:
        pdf_reader = PyPDF2.PdfFileReader(f)
        if page_num == 0:
            # Rotate all pages
            page_numbers = pdf_reader.getNumPages()
        else:
            page_numbers = page_num
        for page_num in range(page_numbers):
            page_obj = pdf_reader.getPage(page_num)
            page_obj.rotateClockwise(degrees)
            pdf_writer.addPage(page_obj)
        pdf_writer.write(o)


def merge_pdf(*args) -> None:
    pdf_writer = PyPDF2.PdfFileWriter()
    output_file = Path(args[0]).with_stem(Path(args[0]).stem + 'merged.pdf')
    with open(output_file, 'wb') as o:
        for arg in args:
            with open(arg, 'rb') as f:
                pdf_reader = PyPDF2.PdfFileReader(f)
                page_nums = pdf_reader.getNumPages()
                for pagenum in range(page_nums):
                    page_obj = pdf_reader.getPage(pagenum)
                    pdf_writer.addPage(page_obj)
        pdf_writer.write(o)
