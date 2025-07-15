import os
import win32com.client

def refresh_excel_file(excel_file_path):
    file = win32com.client.Dispatch('Excel.Application')
    file.Visible = 0
    book = file.Workbooks.open(excel_file_path)
    book.RefreshAll()
    book.Save()
    file.Quit()
