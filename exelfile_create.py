from xlwt import Workbook
from datetime import datetime
from table import *
from meteor_data_class import MeteorDataEntry

def write_filtered_results_to_excel_file(fileEntry): # writes meteor entries and headers to an excel file
    '''
    This is the docstring for the write filtered results to excel file function
    This function creates the excel file and runs the functions that populate it with the filtered 
    meteorite data

    Parameters:
        - fileEntry is an object that is used in functions run in this function

    Returns:
        - This function does not return
    '''
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
    '''
    This is the docstring for the excel final exec function
    This function does the final addition to the excel file, adding the new file name

    Parameters:
        - excel_workbook is the excel object from which the excel file is created

    Returns:
        - This function does not return
    '''
    clean_timestamp_str = get_clean_datetime_string()
    excel_workbook.save(f'{clean_timestamp_str}.xls')
    # confirmation message
    print(f'\n\033[92mFiltered output sent to "{clean_timestamp_str}.xls"\033[0m')

def file_store(fileEntry, meteorite_data_list): # stores the text file contents
    '''
    This is the docstring for the file_store function
    This function opens the inputted text file and stores the filtered meteorite entries in a list

    Parameters:
        - fileEntry contains the user inputted text file name and mode to open it with

        - meteorite_data_list is a list for which the filtered meteorite entries are stored

    Returns:
        - This function returns meteorite_data_list which contains the filtered meteorite data entries
    '''
    with open(fileEntry.textfile, fileEntry.mode) as f: # gets all the filtered meteorite objects
        next(f) # skips first line of text in txt file
        meteorite_data_list = createMeteorEntries(fileEntry, meteorite_data_list, f)
        return meteorite_data_list

def get_headers(headers, filtered_data_sheet, index): # writes all the headers to the excel spreadsheet
    '''
    This is the docstring for the get headers function
    This function writes the headers to the excel file for all the data categories

    Parameters:
        - headers is a list that contains all the data headers for the excel file

        - filtered_data_sheet is the excel spreadsheet

        - index is an incrementer that helps position each header at the correct index in the excel file

    Returns:
        - This function does not return
    '''
    for name in headers:
        # write top row of the Excel output sheet -- __.write(row, column, value)
        filtered_data_sheet.write(0, index, name)
        index += 1

def gen_excel_file(meteorite_data_list, filtered_data_sheet): # writes the meteor entries to the excel file
    '''
    This is the docstring for the get excel file function
    This function writes all the filtered meteorite entries to the excel file

    Parameters:
        - meteorite_data_list is a list that contains all the filtered meteorite entries

        - filtered_data_sheet is the excel spreadsheet

    Returns:
        - This function does not return
    '''
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
    '''
    This is the docstring for the get clean datetime string function
    This function gets the file name for the excel file which is the current date and time

    Parameters:
        No Parameters

    Returns:
        - This function returns a string that is the current date and time
    '''
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str