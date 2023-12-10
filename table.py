from meteor_data_class import MeteorDataEntry

'''
table.py contains all the functions that format the data and filter through the data to produce the final table 
'''

def createMeteorEntries(fileEntry, final_list, f): # uses user input data to create meteor data entries for either mass or year
    for line in f: # parses through every line in the text file
        line.strip()
        data_list = line.split('\t')
        entry_filter(fileEntry, final_list, data_list)
    return final_list

def entry_filter(fileEntry, final_list, data_list): # filters to create entries
    try: 
        datachooser = 0
        datachooser = chooseCategory(datachooser, fileEntry) 
        if float(data_list[datachooser]) >= int(fileEntry.lower_bound) and float(data_list[datachooser]) <= int(fileEntry.upper_bound): # checks the mass of each entry and limits
            final_list.append(createMeteorEntry(data_list))
    except:
        pass

def createMeteorEntry(data_list): # creates meteor data entry
    MeteorEntry = MeteorDataEntry(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6],
                  data_list[7], data_list[8], data_list[9], data_list[10], data_list[11])
    return MeteorEntry
    
def chooseCategory(datachooser, fileEntry): # picks mass or year category
    datachooser = 0 
    if (fileEntry.titleholder == "MASS"):
        datachooser = 4 
    else:
        datachooser = 6 
    return datachooser

def table_footer():
    print(400*"=") # creates a divider
    print("\n") 

def parseIndex(fileEntry): # returns the index that determines weather year or mass is chosen from Meteor Entries to go into the table
    if fileEntry.titleholder == "MASS":
        return 4
    if fileEntry.titleholder == "YEAR":
        return 6

# Prints out table in terminal
def printTable(final_list, fileEntry, entry_index): # THIS FUNCTION ONLY PRINTS TABLE PROPERLY IN PYCHARM
    counter = 0
    table_headers()
    for item in final_list: # parses through all Meteor Entries
        meteorEntryList = list(item.get_data().values()) # creates a list that holds all the data entry information
        if float(meteorEntryList[entry_index]) <= int(fileEntry.upper_bound) and float(meteorEntryList[entry_index]) >= int(fileEntry.lower_bound): # checks for mass to print out to the table
            counter += 1 # increments counter to show line count for printed entries
            printMeteorEntry(meteorEntryList, counter)
    table_footer() # creates a footer for the table

def printMeteorEntry(meteorEntryList, counter): # prints meteor entries into the table
    if counter > 9:
        print(str(counter) + 9*" ", end="")
    else:
        print(str(counter) + 10*" ", end="")
    for data_point in range(12):
        print(meteorEntryList[data_point] + (25-int(len(meteorEntryList[data_point])))*" " + 8*" ", end="") 
    print("\n")

def table_headers(): # prints out table headers
    headers = ["NAME", "ID", "NAMETYPE", "RECCLASS", "MASS", "FALL", "YEAR", "RECLAT", "RECLONG", "GEOLOCATION", "STATES", "COUNTIES"]
    print(11*" ", end="")
    for header in headers:
        print(header + (25 - len(header)) * " " + 8 * " ", end="")  
    print("\n")
    print(400 * "=" + "\n")

        

