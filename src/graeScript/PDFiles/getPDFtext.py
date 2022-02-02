'''Extracting Text from PDF'''
import fitz
from graeScript import outfile_path


class PdfContent:
    file_modes = ('text', 'html', 'json', 'rawjson', 'xhtml', 'xml')
    non_file_modes = ('blocks', 'dict', 'rawdict', 'words')

    def __init__(self, file) -> None:
        self.file = file
        doc = fitz.open(file)
        self.page_num = doc.page_count
        self.toc = doc.get_toc()
        self.metadata = doc.metadata
        doc.close()

    def to_file(self, outfile, *, mode='text', pgstart=1,
                pgstop=None, pgstep=1):
        if mode not in self.file_modes:
            print(f'Mode must be one of {", ".join(self.file_modes)}.')
            raise SystemExit
        doc = fitz.open(self.file)
        if not pgstop:
            pgstop = doc.page_count
        with open(outfile_path() / outfile, 'wb') as f:
            for page in doc.pages(pgstart, pgstop, pgstep):
                text = page.get_text(mode).encode('utf8')
                f.write(text)
                f.write(bytes((12,)))
        doc.close()

    def get(self, *, mode='text', pgstart=1, pgstop=None, pgstep=1):
        if mode not in self.file_modes and mode not in self.non_file_modes:
            print(f'Mode must be one of {", ".join(self.file_modes)},'
                  f' {", ".join(self.non_file_modes)}.')
            raise SystemExit
        doc = fitz.open(self.file)
        if not pgstop:
            pgstop = doc.page_count
        text = []
        for page in doc.pages(pgstart, pgstop, pgstep):
            text.append(page.get_text(mode))
        doc.close()
        return text
