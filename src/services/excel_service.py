import os
import shutil
import openpyxl
import traceback
from config import Config

from  utils.logger import get_logger

logger = get_logger()

config = Config()
def copy_template():
    try:
        logger.info("Inside the function: copy_template")
        template_dir = config.TEMPLATE_FOLDER
        artifact_fld = os.path.join(config.ARTIFACTS_FOLDER, "tmp")
        if os.path.exists(artifact_fld):
            shutil.rmtree(artifact_fld)
        os.makedirs(artifact_fld, exist_ok=True)
        template_file_name = os.listdir(template_dir)[0]
        source_file = os.path.join(template_dir , template_file_name)
        destination_file = os.path.join(artifact_fld , template_file_name)
        shutil.copyfile(source_file, destination_file)
        logger.info("Template file moved successfully ")

    except Exception as e:
        error_details = traceback.format_exc()
        logger.error(error_details)
        print(error_details)
        return {"status": 500, "message": error_details}

def copy_sheet(source_wb, dest_wb, source_sheet_name, dest_sheet_name):
    source_sheet = source_wb[source_sheet_name]
    dest_sheet = dest_wb.create_sheet(dest_sheet_name)
    for row in source_sheet.iter_rows():
        for cell in row:
            dest_sheet[cell.coordinate].value = cell.value



def copy_input():

    # Give the location of the file
    input_fld = Config.INPUT_FOLDER
    input_files = os.listdir(input_fld)[0]
    input_path = os.path.join(input_fld,input_files )
    source_wb = openpyxl.load_workbook(input_path)
    input_sheet_name = "input"

    template_dir = config.TEMPLATE_FOLDER
    artifact_fld = os.path.join(config.ARTIFACTS_FOLDER, "tmp")
    template_file_name = os.listdir(artifact_fld)[0]
    template_file_path = os.path.join(template_dir, 'tmp' ,template_file_name )
    destination_wb = openpyxl.load_workbook(template_file_path)

    copy_sheet(source_wb, destination_wb, Config.TEMPLATE_INPUT_SHEET_NAME, input_sheet_name)

    destination_file_name = ""
    destination_wb.save(destination_file_name)
    # refresh excel 



if __name__ == "__main__":
    copy_template()


