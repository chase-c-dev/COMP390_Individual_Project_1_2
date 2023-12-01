from meteor_data_class import MeteorDataEntry

'''
table.py contains all the functions that format the data and filter through the data to produce the final table 
'''

def createMeteorEntries(fileEntry, final_list, f): # uses user input data to create meteor data entries for either mass or year
    for line in f: # parses through every line in the text file
        line.strip()
        data_list = line.split('\t')
        try: 
            datachooser = 0 # determines weather mass or year data is being used, 1 for mass and 2 for year
            if (fileEntry.titleholder == "MASS"):
                datachooser = 4 
            else:
                datachooser = 6    
            if float(data_list[datachooser]) >= int(fileEntry.lower_bound) and float(data_list[datachooser]) <= int(fileEntry.upper_bound): # checks the mass of each entry and limits
                MeteorEntry = MeteorDataEntry(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6],
                data_list[7], data_list[8], data_list[9], data_list[10], data_list[11]) # creates new meteor entry object
                final_list.append(MeteorEntry)
        except:
            pass
    
    return final_list

def table_header(fileEntry): # creates the header for the table
    print(10*" " + 'NAME' + 30*" " + fileEntry.titleholder) 
    print(80*"=") # creates a divider

def table_footer():
    print(80*"=") # creates a divider
    print("\n") 

def parseIndex(fileEntry): # returns the index that determines weather year or mass is chosen from Meteor Entries to go into the table
    if fileEntry.titleholder == "MASS":
        return 4
    if fileEntry.titleholder == "YEAR":
        return 6

def printTable(final_list, fileEntry, entry_index):
    counter = 0
    for item in final_list: # parses through all Meteor Entries
        meteorEntryList = list(item.get_data().values()) # creates a list that holds all the data entry information
        if float(meteorEntryList[entry_index]) <= int(fileEntry.upper_bound) and float(meteorEntryList[entry_index]) >= int(fileEntry.lower_bound): # checks for mass to print out to the table
            counter += 1 # increments counter to show line count for printed entries
            printMeteorEntry(meteorEntryList, counter, entry_index)
    table_footer() # creates a footer for the table

def printMeteorEntry(meteorEntryList, counter, entry_index): # prints meteor entries into the table
    if counter > 9: # if counter is greater than 9 change spacing, used for correcting spacing when line numbers are over 9
        print(str(counter) + 9*" " + meteorEntryList[0] + (25-int(len(meteorEntryList[0])))*" " + 8*" " + meteorEntryList[entry_index]) # prints the data entries for mass
    else: # else keep spacing constant
        print(str(counter) + 10*" " + meteorEntryList[0] + (25-int(len(meteorEntryList[0])))*" " + 8*" " + meteorEntryList[entry_index])

