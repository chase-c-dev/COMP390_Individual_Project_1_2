from meteor_data_class import MeteorDataEntry
from terminaltext import *
from file_entry_class import FileDataEntry
from table import *
from textfile_create import *
from exelfile_create import *

# Project 1.2 For Software Engineering

def inputmenu():
    '''
    This is the docstring for the input menu function. 
    This function runs all the functions that generate the user prompts

    Parameters:
    - There are no parameters for this function

    Returns:
    - This function does not return
    '''
    fileEntry = FileDataEntry("", "", "", "", "")
    # welcome message
    welcome_message()
    # prompt for file name
    #fileEntry.textfile = file_data_prompter(fileEntry.textfile, "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit", "Target file: ")
    file_path_prompt(fileEntry)
    # prompt for mode to open up file
    mode_prompt(fileEntry)
    # prompts for both lower and upper bounds as well as for year or mass
    dataFiltering(fileEntry)
    # formats data into a table
    choose_output_result_type(fileEntry)

def file_path_prompt(fileEntry):
    '''
    This is the docstring for the file path prompt function. 
    This function runs the function that generates the prompt for the input file

    Parameters:
    - This function takes fileEntry as a parameter because 
      the function it runs utilize this object

    Returns:
    - This function does not return
    '''
    file_path_data_prompter(fileEntry, "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit", "Target file: ")

def mode_prompt(fileEntry):
    '''
    This is the docstring for the mode prompt function. 
    This function runs the function that generates the prompt for the mode

    Parameters:
    - This function takes fileEntry as a parameter because 
      the function it runs utilize this object 

    Returns:
    - This function does not return
    '''
    file_mode_data_prompter(fileEntry, 'What mode would you like to open up the file with\n' 
        '"r" - open for reading (default)\n'
        '"m" - open for writing, truncating the file first (WARNING: this mode will delete the contents of an existing file)\n'
        '"x" - open for exclusive creation, failing if the file already exists\n'
        '"a" - open for writing, appending to the end of file if it exists\n'
        '"b" - binary mode\n'
        '"t" - text mode(default)\n'
        '"+" - open for updating (reading and writing)\n'
        "Enter >q or >Q to quit\n", "File Mode: ")


def filterfile(fileEntry):
    '''
    This is the docstring for the filter file function. 
    This function opens up the input file and stores the filtered meteor entries in a list
    After doing this tableCreate is ran with the filtered meteorite entry list

    Parameters:
    - This function takes fileEntry as a parameter because 
      the functions it runs utilize this object, this object is also
      used to get the file path and mode to open the file

    Returns:
    - This function does not return
    '''
    final_list = [] # stores the sorted meteor data entries
    with open(fileEntry.textfile, fileEntry.mode) as f:
        next(f) # skips first line of text in txt file
        final_list = createMeteorEntries(fileEntry, final_list, f) # creates meteor entries for either all mass or year data

    tableCreate(final_list, fileEntry) # creates the table


def tableCreate(final_list, fileEntry): # creates the tables in the terminal
    '''
    This is the docstring for the table create function. 
    This function creates the table that will be printed to the terminal

    Parameters:
    - This function takes fileEntry as a parameter because 
      the functions it runs utilize this object 

    - This function takes final_list as a parameter because this stores all the
      filtered meteorsite entries that can be used to generate the table

    Returns:
    - This function does not return
    '''
    indexholder = parseIndex(fileEntry)
    printTable(final_list, fileEntry, indexholder) # prints out table into terminal


def choose_output_result_type(fileEntry): # prompts user for options to output file data
    '''
    This is the docstring for choosing the output type function. 
    This function runs the functions based off user input that either print to terminal,
    write to a text file or generate an excel file

    Parameters:
    - This function takes fileEntry as a parameter because 
      the functions it runs utilize this object 

    Returns:
    - This function does not return
    '''
    output_type = output_result_type_prompt("", fileEntry)
    filterfile(fileEntry)
    if int(output_type) == 2:
        create_text_file(fileEntry)
    if int(output_type) == 3:
        write_filtered_results_to_excel_file(fileEntry)

if __name__ == "__main__":
    inputmenu() # runs the program