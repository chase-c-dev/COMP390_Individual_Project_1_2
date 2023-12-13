from meteor_data_class import MeteorDataEntry

'''
table.py contains all the functions that format the data and filter through the data to produce the final table 
'''

def createMeteorEntries(fileEntry, final_list, f): # uses user input data to create meteor data entries for either mass or year
    '''
    This is the docstring for the create meteor entries function
    This function creates the filtered meteor data entries and stores them in a list

    Parameters:
        - fileEntry is an object that is used by other functions called within this function

        - final_list stores the meteor entries 

        - f contains the data from the inputted text file

    Returns:
        - This function returns final_list which is a list of the filtered meteor entries
    '''
    for line in f: # parses through every line in the text file
        line.strip()
        data_list = line.split('\t')
        entry_filter(fileEntry, final_list, data_list)
    return final_list

def entry_filter(fileEntry, final_list, data_list): # filters to create entries
    '''
    This is the docstring for the entry filter function
    This function filters through the meteor entries to match the user input specifications
    matched meteor entries are appended to the final_list

    Parameters:
        - fileEntry is used to get the lower_bound and upper_bound for the conditional

        - final_list stores the selected meteor entries

        - data_list contains a line from the input text file in the form of a python list

    Returns:
        - This function does not return
    '''
    try: 
        datachooser = 0
        datachooser = chooseCategory(datachooser, fileEntry) 
        if float(data_list[datachooser]) >= int(fileEntry.lower_bound) and float(data_list[datachooser]) <= int(fileEntry.upper_bound): # checks the mass of each entry and limits
            final_list.append(createMeteorEntry(data_list))
    except:
        pass

def createMeteorEntry(data_list): # creates meteor data entry
    '''
    This is the docstring for the create meteor entry function
    This function creates a meteor entry based off of the data_list input and returns the entry

    Parameters:
        - data_list contains the meteorite data to be added to a new MeteorDataEntry object

    Returns:
        - This function returns MeteorEntry which is a MeteorDataEntry object containing meteorite data
    '''
    MeteorEntry = MeteorDataEntry(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6],
                  data_list[7], data_list[8], data_list[9], data_list[10], data_list[11])
    return MeteorEntry
    
def chooseCategory(datachooser, fileEntry): # picks mass or year category
    '''
    This is the docstring for the choose category function
    This function determines what index will be used for data selection from meteorite data lists 

    Parameters:
        - datachooser is the variable that stores the index to return 

        - fileEntry is an object that contains the user inputted title used in the conditional to determine the index 

    Returns:
        - This function returns datachooser which is a index used to filter meteorite entries off of either mass or year
    '''
    datachooser = 0 
    if (fileEntry.titleholder == "MASS"):
        datachooser = 4 
    else:
        datachooser = 6 
    return datachooser

def table_footer():
    '''
    This is the docstring for the table footer function
    This function prints the table footer for the print to terminal table

    Parameters:
        No Parameters

    Returns:
        - This function returns nothing
    '''
    print(400*"=") # creates a divider
    print("\n") 

def parseIndex(fileEntry): # returns the index that determines weather year or mass is chosen from Meteor Entries to go into the table
    '''
    This is the docstring for the parse index function
    This function returns an index that determines weather year or mass is chosen from Meteor Entries
    to go into the table

    Parameters:
        - fileEntry is an object and contains what the user inputted for title, important for the conditional

    Returns:
        - returns an integer that is an index for filtering meteor data as index 4 is mass and index 6 is year
    '''
    if fileEntry.titleholder == "MASS":
        return 4
    if fileEntry.titleholder == "YEAR":
        return 6

# Prints out table in terminal
def printTable(final_list, fileEntry, entry_index): # THIS FUNCTION ONLY PRINTS TABLE PROPERLY IN PYCHARM
    '''
    This is the docsrting for the print table function
    This function prints a table to the terminal containing all filtered meteorite data

    Parameters:
        - final_list contains all filtered meteorite data entries

        - fileEntry contains the lower bound and upper bound data for checking meteor entries

        - entry_index contains index to check either mass or year for filtering

    Returns:
        - This function does not return
    '''
    counter = 0
    table_headers()
    for item in final_list: # parses through all Meteor Entries
        meteorEntryList = list(item.get_data().values()) # creates a list that holds all the data entry information
        if float(meteorEntryList[entry_index]) <= int(fileEntry.upper_bound) and float(meteorEntryList[entry_index]) >= int(fileEntry.lower_bound): # checks for mass to print out to the table
            counter += 1 # increments counter to show line count for printed entries
            printMeteorEntry(meteorEntryList, counter)
    table_footer() # creates a footer for the table

def printMeteorEntry(meteorEntryList, counter): # prints meteor entries into the table
    '''
    This is the docstring for the print meteor entry function
    This function prints a meteor entry while formatting it to fit in the table properly 

    Parameters:
        - meteorEntryList contains a list of all the info in meteor data entry

        - counter contains the line number for the meteor entry

    Returns:
        - This function does not return
    '''
    if counter > 9:
        print(str(counter) + 9*" ", end="")
    else:
        print(str(counter) + 10*" ", end="")
    for data_point in range(12):
        print(meteorEntryList[data_point] + (25-int(len(meteorEntryList[data_point])))*" " + 8*" ", end="") 
    print("\n")

def table_headers(): # prints out table headers
    '''
    This is the docstring for table headers
    This function generates the headers for the terminal printed table

    Parameters:
        No Parameters

    Returns:
        - This function does not return anything
    '''
    headers = ["NAME", "ID", "NAMETYPE", "RECCLASS", "MASS", "FALL", "YEAR", "RECLAT", "RECLONG", "GEOLOCATION", "STATES", "COUNTIES"]
    print(11*" ", end="")
    for header in headers:
        print(header + (25 - len(header)) * " " + 8 * " ", end="")  
    print("\n")
    print(400 * "=" + "\n")

        

