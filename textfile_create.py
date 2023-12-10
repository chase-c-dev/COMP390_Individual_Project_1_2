from datetime import datetime
from meteor_data_class import MeteorDataEntry

def create_text_file(fileEntry): # creates txt file and writes to it
    txt_name = get_clean_datetime_string() + ".txt"
    data_for_textfile = get_filtered_meteor_data_fortxt(fileEntry)
    with open(txt_name, "w") as file:
        for line in data_for_textfile:
            file.write(line)
            

def get_filtered_meteor_data_fortxt(fileEntry):
    data_for_textfile = []
    line_numbers = []
    header = ""
    with open(fileEntry.textfile, fileEntry.mode) as f:
        header = f.readline()
        next(f)
        line_numbers = getLineNumbers(fileEntry, line_numbers, f)
    data_for_textfile = get_all_text_data(line_numbers, header, fileEntry)
    return data_for_textfile

def getLineNumbers(fileEntry, line_numbers, f): # gets the line numbers for the data
    line_counter = 0
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
                line_numbers.append(line_counter)
            line_counter += 1
        except:
            line_counter += 1
            pass

    return line_numbers # returns the line numbers in the txt for the data needed
    
def get_all_text_data(line_numbers, header, fileEntry): # gets all the data to write to the new textfile
    text_data = []
    text_data.append(header)
    line_counter = 0
    with open(fileEntry.textfile, fileEntry.mode) as f:
        next(f)
        for line in f:
            for line_number in line_numbers:
                if line_counter == line_number:
                    text_data.append(line)
            line_counter += 1
    return text_data

def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str
