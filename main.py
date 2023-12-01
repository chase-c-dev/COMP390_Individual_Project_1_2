from meteor_data_class import MeteorDataEntry
from terminaltext import *
from file_entry_class import FileDataEntry
from table import *

# Project 1.1 For Software Engineering

def inputmenu():
    fileEntry = FileDataEntry("", "", "", "", "")
    # welcome message
    welcome_message()
    # prompt for file name
    fileEntry.textfile = file_data_prompter(fileEntry.textfile, "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit", "Target file: ")
    #prompt for mode to open up file
    fileEntry.mode = file_data_prompter(fileEntry.mode, 'What mode would you like to open up the file with\n' 
                 '"r" - open for reading (default)\n'
                 '"m" - open for writing, truncating the file first\n'
                 '"x" - open for exclusive creation, failing if the file already exists\n'
                 '"a" - open for writing, appending to the end of file if it exists\n'
                 '"b" - binary mode\n'
                 '"t" - text mode(default)\n'
                 '"+" - open for updating (reading and writing)\n'
                 "Enter >q or >Q to quit\n", "File Mode: ")
    
    dataFiltering(fileEntry) # prompts for both lower and upper bounds as well as for year or mass

    filterfile(fileEntry) # formats data into a table

# remember for lower bound and upper bound you have to convert it to an int
def filterfile(fileEntry):
    final_list = [] # stores the sorted meteor data entries
    with open(fileEntry.textfile, fileEntry.mode) as f:
        next(f) # skips first line of text in txt file
        final_list = createMeteorEntries(fileEntry, final_list, f) # creates meteor entries for either all mass or year data
          
    headers = ['NAME', fileEntry.titleholder] # headers for the table categories
    textFormatter(headers, final_list, fileEntry)
   

def textFormatter(headers, final_list, fileEntry): # creates the tables in the terminal
    indexholder = 0
    if headers[1] == "MASS":
        indexholder = 4
    if headers[1] == "YEAR":
        indexholder = 6
    print(10*" " + 'NAME' + 30*" " + headers[1]) # formats the headers for name and mass table
    print(80*"=") # creates a divider
    counter = 0
    for item in final_list: # parses through all the sorted data entries
        holder = list(item.get_data().values()) # creates a list that holds all the data entry information
        if float(holder[indexholder]) <= int(fileEntry.upper_bound) and float(holder[indexholder]) >= int(fileEntry.lower_bound): # checks for mass to print out to the table
            counter += 1 # increments counter to show line count for printed entries
            if counter > 9: # if counter is greater than 9 change spacing, used for correcting spacing when line numbers are over 9
                print(str(counter) + 9*" " + holder[0] + (25-int(len(holder[0])))*" " + 8*" " + holder[indexholder]) # prints the data entries for mass
            else: # else keep spacing constant
                print(str(counter) + 10*" " + holder[0] + (25-int(len(holder[0])))*" " + 8*" " + holder[indexholder]) # prints the data entries for mass
    print(80*"=") # creates a divider
    print("\n") # creates a new line for separation of both tables

if __name__ == "__main__":
    inputmenu() # runs the program