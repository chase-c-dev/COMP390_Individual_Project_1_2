from xlwt import Workbook
from datetime import datetime
from table import *
from meteor_data_class import MeteorDataEntry

def write_filtered_results_to_excel_file(fileEntry): # writes meteor entries and headers to an excel file
    excel_workbook = Workbook()
    filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')
    headers = ["NAME", "ID", "NAMETYPE", "RECCLASS", "MASS", "FALL", "YEAR", "RECLAT", "RECLONG", "GEOLOCATION", "STATES", "COUNTIES"]
    index = 0
    meteorite_data_list = []

    file_store(fileEntry, meteorite_data_list)
    
    get_headers(headers, filtered_data_sheet, index)

    gen_excel_file(meteorite_data_list, filtered_data_sheet)

    excel_final_exec(excel_workbook)

def excel_final_exec(excel_workbook): # does final executions for excel spreadsheet
    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    # confirmation message
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')

def file_store(fileEntry, meteorite_data_list): # stores the text file contents
    with open(fileEntry.textfile, fileEntry.mode) as f: # gets all the filtered meteorite objects
        next(f) # skips first line of text in txt file
        meteorite_data_list = createMeteorEntries(fileEntry, meteorite_data_list, f)
        return meteorite_data_list

def get_headers(headers, filtered_data_sheet, index): # writes all the headers to the excel spreadsheet
     for name in headers:
        # write top row of the Excel output sheet -- __.write(row, column, value)
        filtered_data_sheet.write(0, index, name)
        index += 1

def gen_excel_file(meteorite_data_list, filtered_data_sheet): # writes the meteor entries to the excel file
    for index in range(len(meteorite_data_list)):
        # get the current meteorite object
        current_meteorite_record_obj = meteorite_data_list[index]
        # get a Python list with all 12 of the current meteorite object's attributes
        # extract_data_from_meteorite_object() should return a list of 12 values
        attribute_list = list(current_meteorite_record_obj.get_data().values())
        # loop through the attribute strings in the attribute list
        for attr_index in range(len(attribute_list)):
            # write each row of the Excel output sheet -- __.write(row, column, value)
            filtered_data_sheet.write(index + 1, attr_index, attribute_list[attr_index])

def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str