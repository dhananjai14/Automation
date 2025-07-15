import os
import win32com.client

def refresh_excel_file(excel_file_path):
    file = win32com.client.Dispatch('Excel.Application')
    file.Visible = 0
    book = file.Workbooks.open(excel_file_path)
    book.RefreshAll()
    book.Save()
    file.Quit()


def copy_sheet(source_wb, dest_wb, source_sheet_name, dest_sheet_name):
    source_sheet = source_wb[source_sheet_name]
    dest_sheet = dest_wb[dest_sheet_name]
    for row in source_sheet.iter_rows():
        for cell in row:
            dest_sheet[cell.coordinate].value = cell.value