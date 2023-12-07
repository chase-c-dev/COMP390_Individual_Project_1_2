from meteor_data_class import MeteorDataEntry
from terminaltext import *
from file_entry_class import FileDataEntry
from table import *

# Project 1.2 For Software Engineering

def inputmenu():
    fileEntry = FileDataEntry("", "", "", "", "")
    # welcome message
    welcome_message()
    # prompt for file name
    fileEntry.textfile = file_data_prompter(fileEntry.textfile, "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit", "Target file: ")
    # prompt for mode to open up file
    fileEntry.mode = file_data_prompter(fileEntry.mode, 'What mode would you like to open up the file with\n' 
                 '"r" - open for reading (default)\n'
                 '"m" - open for writing, truncating the file first (WARNING: this mode will delete the contents of an existing file)\n'
                 '"x" - open for exclusive creation, failing if the file already exists\n'
                 '"a" - open for writing, appending to the end of file if it exists\n'
                 '"b" - binary mode\n'
                 '"t" - text mode(default)\n'
                 '"+" - open for updating (reading and writing)\n'
                 "Enter >q or >Q to quit\n", "File Mode: ")
    # prompts for both lower and upper bounds as well as for year or mass
    dataFiltering(fileEntry) 
    # formats data into a table
    filterfile(fileEntry) 

def filterfile(fileEntry):
    final_list = [] # stores the sorted meteor data entries
    with open(fileEntry.textfile, fileEntry.mode) as f:
        next(f) # skips first line of text in txt file
        final_list = createMeteorEntries(fileEntry, final_list, f) # creates meteor entries for either all mass or year data
          
    tableCreate(final_list, fileEntry) # creates the table
   

def tableCreate(final_list, fileEntry): # creates the tables in the terminal
    indexholder = parseIndex(fileEntry)
    table_header(fileEntry) # creates the header for the table
    printTable(final_list, fileEntry, indexholder)

if __name__ == "__main__":
    inputmenu() # runs the program