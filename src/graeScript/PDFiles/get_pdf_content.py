'''Extracting Text from PDF'''
from enum import Enum
from pathlib import Path
import fitz
from graeScript import outfile_path


class FileMode(Enum):
    """
    PDF output text modes that work with sending to file.

    From Fitz/pymupdf:
        https://pymupdf.readthedocs.io/en/latest/page.html?highlight=get_text#Page.get_text
    """
    text = 0
    html = 1
    json = 2
    rawjson = 3
    xhtml = 4
    xml = 5


class NonFileMode(Enum):
    """
    PDF output text modes that do not work with sending to file.

    From Fitz/pymupdf:
        https://pymupdf.readthedocs.io/en/latest/page.html?highlight=get_text#Page.get_text
    """
    blocks = 0
    dict = 1
    rawdict = 2
    words = 3


class PdfContent:
    file_modes = ('text', 'html', 'json', 'rawjson', 'xhtml', 'xml')
    non_file_modes = ('blocks', 'dict', 'rawdict', 'words')

    def __init__(self, file: str | Path) -> None:
        self.filepath = file
        doc = fitz.open(file)
        self.page_num = doc.page_count
        self.toc = doc.get_toc()
        self.metadata = doc.metadata
        doc.close()

    def to_file(self, *, outfile: str | Path = None,
                mode: str | FileMode = 'text', pgstart: int = 0,
                pgstop: int = None, pgstep: int = 1, skippics=False):
        """
        Send PDF text/contents to output file in the format of `mode`.

        Args:
            outfile (str | Path): The output file path including extension
            mode (str | FileMode, optional): The mode of the PDF output.
                Defaults to 'text'. See Fitz docs: https://bit.ly/3FiUbHf
            pgstart (int, optional): The page at which to start. Defaults to 0.
            pgstop (int, optional): The page at which to stop. Defaults to
                None.
            pgstep (int, optional): The page steps. Defaults to 1 which
                outputs every page from pgstart to pgstop.

        Raises:
            SystemExit: If the mode is not a valid file mode.
        """
        if isinstance(mode, (FileMode)):
            # Set string name from FileMode Enum.
            mode = mode.name
        if mode not in self.file_modes:
            # Exit program if mode doesn't match filemode.
            print(f'Mode must be one of {", ".join(self.file_modes)}.')
            raise SystemExit
        if not outfile:
            # Set output file name if not provided.
            outfile = self.filepath.with_suffix(f'.{mode}').parts[-1]

        doc = fitz.open(self.filepath)
        if not pgstop:
            pgstop = doc.page_count
        with open(outfile_path() / outfile, 'wb') as f:
            for page in doc.pages(pgstart, pgstop, pgstep):
                if skippics:
                    text = page.get_text(mode,  flags=fitz.TEXTFLAGS_HTML &
                                         ~fitz.TEXT_PRESERVE_IMAGES
                                         ).encode('utf-8')
                else:
                    text = page.get_text(mode).encode('utf-8')
                f.write(text)
                f.write(bytes((12,)))
        doc.close()

    def get(self, *, mode: str | FileMode | NonFileMode = 'text',
            pgstart: int = 0, pgstop: int = None, pgstep: int = 1):
        """
        Return PDF text/contents in the format of `mode`.

        Args:
            mode (str | FileMode | NonFileMode, optional): The mode of the PDF
                output. Defaults to 'text'. See Fitz docs:
                https://bit.ly/3FiUbHf
            pgstart (int, optional): The page at which to start. Defaults to 0.
            pgstop (int, optional): The page at which to stop. Defaults to
                None.
            pgstep (int, optional): The page steps. Defaults to 1 which
                outputs every page from pgstart to pgstop.

        Raises:
            SystemExit: If mode is not a FileMode or NonFileMode
        """
        if isinstance(mode, (FileMode, NonFileMode)):
            mode = mode.name
        if mode not in self.file_modes and mode not in self.non_file_modes:
            print(f'Mode must be one of {", ".join(self.file_modes)},'
                  f' {", ".join(self.non_file_modes)}.')
            raise SystemExit
        doc = fitz.open(self.filepath)
        if not pgstop:
            pgstop = doc.page_count
        text = []
        for page in doc.pages(pgstart, pgstop, pgstep):
            text.append(page.get_text(mode))
        doc.close()
        return text


if __name__ == '__main__':
    pass
