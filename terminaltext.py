from file_entry_class import FileDataEntry
from table import *
from error_handling import *

'''
termianltext.py contains functions that prompt the user and get the information required to produce the table
all functions involve printing to the terminal and collecting user input
'''


# prints out welcome message
def welcome_message(): 
    print("Welcome to the meteorite filtering program\n") # welcome message
    print("This program allows you to filter NASA meteorite data contained in a text file\n")
    print("The data in the text file must be organized in a specific format\n Required format:\n    Each line of the text file describes a single meteorite.")
    print("    For each meteorite line there must be 12 tab separated data points\n \nPlease follow the prompts to filter the data")       
    print("\nI am the developer, Chase\n")
    print("The release date of this program is October 5th 2023\n")

def file_mode_data_prompter(fileEntry, input_text, output_text): # runs the input menu and the quitCheck function for mode and file name
    fileEntry.mode = input(input_text)
    quitCheckMode(fileEntry.mode, output_text, fileEntry) # checks to see if the program exits or continues

def file_path_data_prompter(fileEntry, input_text, output_text): # runs the input menu and the quitCheck function for mode and file name
    fileEntry.textfile = input(input_text)
    quitCheckFilePath(fileEntry.textfile, output_text, fileEntry) # checks to see if the program exits or continues

def file_bounds_prompter(file_entry, input_text, output_text): # runs the input menu and quit check for filter bounds
    file_entry = input(input_text)
    quitCheckBounds(file_entry, output_text) # checks to see if the program exits or continues
    return file_entry

def exit_check(promptInput): # checks to see if program should exit
    if promptInput == ">q" or promptInput == ">Q": 
        print("The program is now exiting Goodbye!")
        exit() # exits program

def quitCheckFilePath(promptInput, output_text, fileEntry): # checks file path to see if program should quit or if theres an error
    exit_check(promptInput)
    errorcheck(output_text, 1, fileEntry)

def quitCheckMode(promptInput, output_text, fileEntry): # checks mode to see if program should quit or if theres an error
    exit_check(promptInput)
    errorcheck(output_text, 2, fileEntry)
       
# checks to see if program quits or continues for bounds prompts
def quitCheckBounds(promptInput, output_text):
    if promptInput == "Q": 
        print("The program is now exiting Goodbye!")
        exit() # exits program
    else:
        print(output_text + promptInput + "\n") # prints read mode

def errorcheck(output_text, num, fileEntry): # runs error checks for various user input prompts
    if num == 1 and check_file_path(fileEntry, output_text) == False:
        file_path_data_prompter(fileEntry, "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit", "Target file: ")
    if num == 2 and check_for_mode(fileEntry, output_text) == False:
        file_mode_data_prompter(fileEntry, mode_prompt_text(), "File Mode: ")
    if num == 3 and filter_category_check(output_text) == False:
        dataFiltering(fileEntry)
    if num == 4 and check_lower_bound(fileEntry, output_text) == False:
        fileEntry.lower_bound = file_bounds_prompter(fileEntry.lower_bound, "Enter the LOWER limit (inclusive) for the meteor's " + output_text + " , (Enter Q to quit) \n", "Lower Bound: ")
        errorcheck(output_text, 4, fileEntry)
    if num == 5 and check_upper_bound(fileEntry, output_text) == False:
        fileEntry.upper_bound = file_bounds_prompter(fileEntry.upper_bound, "Enter the UPPER limit (inclusive) for the meteor's " + output_text + " , (Enter Q to quit) \n", "Upper Bound: ")
        errorcheck(output_text, 5, fileEntry)
    if num == 6 and check_display_type(output_text, fileEntry) == False:
        output_result_type_prompt(output_text, fileEntry)
    else:
        pass

def mode_prompt_text(): # returns string for mode prompt
    mode_prompt = 'What mode would you like to open up the file with\n' 
    '"r" - open for reading (default)\n'
    '"m" - open for writing, truncating the file first (WARNING: this mode will delete the contents of an existing file)\n'
    '"x" - open for exclusive creation, failing if the file already exists\n'
    '"a" - open for writing, appending to the end of file if it exists\n'
    '"b" - binary mode\n'
    '"t" - text mode(default)\n'
    '"+" - open for updating (reading and writing)\n'
    "Enter >q or >Q to quit\n"
    return mode_prompt
    

def dataFiltering(file_entry): # chooses year, mass or exit based on user input
    data_filter = input("What attribute would you like to filter the data on\n 1. meteor MASS(g)\n 2. The Year the meteor fell to earth\n 3. QUIT\n")
    errorcheck(data_filter, 3, file_entry) # checks user_input for errors
    if data_filter == "3": # exists the program
        print("The program is now exiting Goodbye!")
        exit()
    elif data_filter == "2":
        bounds_prompt(file_entry, "YEAR")
        file_entry.titleholder = "YEAR"
    elif data_filter == "1":
        bounds_prompt(file_entry, "MASS")
        file_entry.titleholder = "MASS"

def bounds_prompt(file_entry, label_text): # prompts for upper and lower bounds of mass or year
    file_entry.lower_bound = file_bounds_prompter(file_entry.lower_bound, "Enter the LOWER limit (inclusive) for the meteor's " + label_text + " , (Enter Q to quit) \n", "Lower Bound: ")
    errorcheck(label_text, 4, file_entry)
    file_entry.upper_bound = file_bounds_prompter(file_entry.upper_bound, "Enter the UPPER limit (inclusive) for the meteor's " + label_text + " , (Enter Q to quit) \n", "Upper Bound: ")
    errorcheck(label_text, 5, file_entry)

def output_result_type_prompt(output_type, fileEntry): # runs prompt for output type
    output_type = input("How would you like to putput the filter results?\n 1. On screen (in terminal)\n 2. To a TEXT file\n 3. To an EXCEL file\n 4. QUIT")
    errorcheck(output_type, 6, fileEntry)
    try:
        if int(output_type) == 4:
            print("The program is now exiting Goodbye!")
            exit()
    except:
        pass
    return output_type




