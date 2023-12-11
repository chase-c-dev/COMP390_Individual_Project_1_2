from datetime import datetime
from meteor_data_class import MeteorDataEntry

def create_text_file(fileEntry): # creates txt file and writes to it
    txt_name = get_clean_datetime_string() + ".txt"
    data_for_textfile = get_filtered_meteor_data_fortxt(fileEntry)
    with open(txt_name, "w") as file:
        for line in data_for_textfile:
            file.write(line)
            

def get_filtered_meteor_data_fortxt(fileEntry): # returns list of data to be written to text file
    data_for_textfile = []
    line_numbers = []
    header = ""
    with open(fileEntry.textfile, fileEntry.mode) as f:
        header = f.readline()
        next(f)
        line_numbers = getLineNumbers(fileEntry, line_numbers, f)
    data_for_textfile = get_all_text_data(line_numbers, header, fileEntry)
    return data_for_textfile

def getLineNumbers(fileEntry, line_numbers, f): # gets the line numbers for all the data to be written
    line_counter = 0
    for line in f: # parses through every line in the text file
        line.strip()
        data_list = line.split('\t')
        datachooser = 0 # determines weather mass or year data is being used, 1 for mass and 2 for year
        line_counter += 1
        datachooser = chooseCategory(datachooser, fileEntry)
        if (LineNumberConditional(data_list, datachooser, fileEntry) == True):
            line_numbers.append(line_counter)
    return line_numbers # returns the line numbers in the txt for the data needed

def LineNumberConditional(data_list, datachooser, fileEntry): # checks user input bounds and returns true for add data and false to skip entry
    try:
        if float(data_list[datachooser]) >= int(fileEntry.lower_bound) and float(data_list[datachooser]) <= int(fileEntry.upper_bound):
            return True
        return False
    except:
        return False

def chooseCategory(datachooser, fileEntry): # picks mass or year category for filter
    datachooser = 0 
    if (fileEntry.titleholder == "MASS"):
        datachooser = 4 
    else:
        datachooser = 6 
    return datachooser
    
def get_all_text_data(line_numbers, header, fileEntry): # gets all the data to write to the new textfile
    text_data = []
    text_data.append(header)
    line_counter = 0
    with open(fileEntry.textfile, fileEntry.mode) as f:
        next(f)
        for line in f:
            add_line_number(text_data, line, search_line_numbers(line_numbers, line_counter))
            line_counter += 1
    return text_data

def add_line_number(text_data, line, add_decider): # adds a line number is provided true
    if add_decider == True:
        text_data.append(line)

def search_line_numbers(line_numbers, line_counter): # returns true if a line number matches
    for line_number in line_numbers:
        if line_counter == line_number:
            return True
        else:
            pass

def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str
