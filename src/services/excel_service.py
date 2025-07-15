import os
import shutil
import openpyxl
import traceback
from config import Config

from  utils.logger import get_logger
from utils.helper import copy_sheet, refresh_excel_file
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



def copy_input():

    # Give the location of the file
    input_fld = Config.INPUT_FOLDER
    input_files = os.listdir(input_fld)[0]
    input_path = os.path.join(input_fld,input_files )
    wb_obj_input = openpyxl.load_workbook(input_path)
    source_sheet_name = config.INPUT_SHEET_NAME
    
    
    template_dir = config.TEMPLATE_FOLDER
    artifact_fld = os.path.join(config.ARTIFACTS_FOLDER, "tmp")
    template_file_name = os.listdir(artifact_fld)[0]
    template_file_path = os.path.join(artifact_fld, template_file_name )   
    wb_obj_template = openpyxl.load_workbook(template_file_path)
    dest_sheet_name = config.TEMPLATE_INPUT_SHEET_NAME
    # copy input 
    copy_sheet(wb_obj_input,wb_obj_template, source_sheet_name, dest_sheet_name )

    result_file_path = os.path.join(config.OUTPUT_FOLDER, config.RESULT_FILE_NAME)

    wb_obj_template.save(filename=result_file_path)
    final_file_path = os.path.join(os.getcwd(), result_file_path)

    refresh_excel_file(final_file_path)

    
if __name__ == "__main__":
    copy_input()


