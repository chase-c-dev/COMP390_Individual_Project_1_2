from xlwt import Workbook
from datetime import datetime
from table import *
from meteor_data_class import MeteorDataEntry

# def write_filtered_results_to_excel_file():
# # Workbook is created
#     excel_workbook = Workbook()
#     # add a sheet to the workbook
#     filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')

#     # write the attribute titles to the top of the sheet
#     index = 0
#     for name in attribute name list [‘name’, ‘id’, ‘nametype’, …]:
#         # write top row of the Excel output sheet -- __.write(row, column, value)
#         filtered_data_sheet.write(0, index, name)
#         index++
#     # loop through all the filtered meteorite objects
#     for index in range(len(filtered_meteorite_object_list):
#         # get the current meteorite object
#         current_meteorite_record_obj = filtered_meteorite_object_list[index]
#         # get a Python list with all 12 of the current meteorite object's attributes
#         # extract_data_from_meteorite_object() should return a list of 12 values
#         attribute_list = extract_data_from_meteorite_object()
#         # loop through the attribute strings in the attribute list
#         for attr_index in range(len(attribute_list)):
#             # write each row of the Excel output sheet -- __.write(row, column, value)
#             filtered_data_sheet.write(index + 1, attr_index, attribute_list[attr_index])
#     clean_timestamp_str = get_clean_datetime_string()
#     excel_workbook.save(f'{clean_timestamp_str}.xls')
#     # confirmation message
#     print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')
# --------------------------------------------------------------------------------------------------------

def write_filtered_results_to_excel_file(fileEntry):
    excel_workbook = Workbook()
    filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')
    headers = ["NAME", "ID", "NAMETYPE", "RECCLASS", "MASS", "FALL", "YEAR", "RECLAT", "RECLONG", "GEOLOCATION", "STATES", "COUNTIES"]
    index = 0
    meteorite_data_list = []
    with open(fileEntry.textfile, fileEntry.mode) as f: # gets all the filtered meteorite objects
        next(f) # skips first line of text in txt file
        meteorite_data_list = createMeteorEntries(fileEntry, meteorite_data_list, f)

    for name in headers:
        # write top row of the Excel output sheet -- __.write(row, column, value)
        filtered_data_sheet.write(0, index, name)
        index += 1
    
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
    
    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    # confirmation message
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')




def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str