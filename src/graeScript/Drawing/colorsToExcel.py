import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.styles import Font
from PIL import ImageColor

from graeScript import outfile_path


def colors_to_excel(new_wb_name, headings_by_col, font_name, head_bold=True):
    # Open Workbook and sheet to copy from
    s_wb = openpyxl.load_workbook(outfile_path() / 'HTMLcolors.xlsx',
                                  data_only=True)
    s_sheet = s_wb.active
    maxrow = s_sheet.max_row
    # Open new, blank Workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    for r in range(1, maxrow+1):
        new_cells_row = {
            heading: sheet[f'{c}{r}'] for c, heading
            in headings_by_col.items()}
        if r == 1:
            for heading, cell in new_cells_row.items():
                cell.font = Font(name=font_name, bold=head_bold)
                cell.value = heading
            continue
        cellvalues = {
            headings_by_col['A']: s_sheet[f'C{r}'].value,  # Group
            headings_by_col['B']: s_sheet[f'A{r}'].value,  # Name
            headings_by_col['C']: (
                f"{ImageColor.getcolor(s_sheet[f'A{r}'].value, 'RGB')}"),
            headings_by_col['D']: s_sheet[f'B{r}'].value,  # HEX
            }

        for heading, cell in new_cells_row.items():
            if heading != 'Color':
                cell.font = Font(name=font_name)
                cell.value = cellvalues[heading]
                continue
            cell.fill = PatternFill(fill_type='solid',
                                    start_color=cellvalues['HEX'].lstrip('#'),
                                    end_color=cellvalues['HEX'].lstrip('#'))
    wb.save(new_wb_name)
