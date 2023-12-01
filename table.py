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

