from meteor_data_class import MeteorDataEntry
from terminaltext import *
from file_entry_class import FileDataEntry

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

    filterfile(fileEntry.titleholder, int(fileEntry.lower_bound), int(fileEntry.upper_bound), fileEntry.mode, fileEntry.textfile) # formats data into a table

def filterfile(title, lower_bound, upper_bound, readmode, targetfile):
    data_list1 = [] # stores the entire base text file
    final_list = [] # stores the sorted meteor data entries
    with open(targetfile, readmode) as f:
        next(f) # skips first line of text in txt file
        for line in f: # parses through every line in the text file
            line.strip()
            data_list1 = line.split('\t')
            try: # tries to perform the following comparisons and skips the line is there is an error via the except clause
                if title == "MASS": # runs code if we are looking for mass table
                    if float(data_list1[4]) >= lower_bound and float(data_list1[4]) <= upper_bound: # checks the mass of each entry and limits
                        MeteorEntry = MeteorDataEntry(data_list1[0], data_list1[1], data_list1[2], data_list1[3], data_list1[4], data_list1[5], data_list1[6],
                        data_list1[7], data_list1[8], data_list1[9], data_list1[10], data_list1[11]) # creates new meteor entry object
                        final_list.append(MeteorEntry) # adds the new entry to the list
                if title == "YEAR": # runs code if we are looking for year table
                    if int(data_list1[6]) >= lower_bound and int(data_list1[6]) <= upper_bound: # checks the year of each entry
                        MeteorEntry = MeteorDataEntry(data_list1[0], data_list1[1], data_list1[2], data_list1[3], data_list1[4], data_list1[5], data_list1[6],
                        data_list1[7], data_list1[8], data_list1[9], data_list1[10], data_list1[11]) # creates new meteor entry object
                        final_list.append(MeteorEntry) # adds the new entry to the list
            except:
                pass
    headers = ['NAME', title] # headers for the table categories
    if title == "MASS":
        textFormatter(headers, final_list, upper_bound, lower_bound)
    elif title == "YEAR":
        textFormatter(headers, final_list, upper_bound, lower_bound)

def textFormatter(headers, final_list, upper_bound, lower_bound): # creates the tables in the terminal
    indexholder = 0
    if headers[1] == "MASS":
        indexholder = 4
    if headers[1] == "YEAR":
        indexholder = 6
    print(10*" " + headers[0] + 30*" " + headers[1]) # formats the headers for name and mass table
    print(80*"=") # creates a divider
    counter = 0
    for item in final_list: # parses through all the sorted data entries
        holder = list(item.get_data().values()) # creates a list that holds all the data entry information
        if float(holder[indexholder]) <= upper_bound and float(holder[indexholder]) >= lower_bound : # checks for mass to print out to the table
            counter += 1 # increments counter to show line count for printed entries
            if counter > 9: # if counter is greater than 9 change spacing, used for correcting spacing when line numbers are over 9
                print(str(counter) + 9*" " + holder[0] + (25-int(len(holder[0])))*" " + 8*" " + holder[indexholder]) # prints the data entries for mass
            else: # else keep spacing constant
                print(str(counter) + 10*" " + holder[0] + (25-int(len(holder[0])))*" " + 8*" " + holder[indexholder]) # prints the data entries for mass
    print(80*"=") # creates a divider
    print("\n") # creates a new line for separation of both tables

if __name__ == "__main__":
    inputmenu() # runs the program