from datetime import datetime
from meteor_data_class import MeteorDataEntry

def create_text_file(fileEntry): # creates txt file and writes to it
    '''
    This is the docstring for the create text file function
    This function writes filtered meteorite data to a text file

    Parameters:
        - fileEntry is an object that is used in functions called in this function

    Returns:
        - This function does not return
    '''
    txt_name = get_clean_datetime_string() + ".txt"
    data_for_textfile = get_filtered_meteor_data_fortxt(fileEntry)
    with open(txt_name, "w") as file:
        for line in data_for_textfile:
            file.write(line)
            

def get_filtered_meteor_data_fortxt(fileEntry): # returns list of data to be written to text file
    '''
    This is the docstring for the get filtered meteor data for text file function
    This function opens up the text file and gets all the filtered meteorite data into a list

    Parameters:
        - fileEntry is used to get the text file name and mode and is used as a parameter in get line numbers 

    Returns:
        - returns a list containing filtered meteorite data
    '''
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
    '''
    This is the docstring for get line numbers function
    This function gets all the line numbers of every meteorite data entry that matches user input 

    Parameters:
        - fileEntry is an object used in functions called in this function

        - line_numbers is a list in which selected line numbers are stored

        - f contains all the data from the inputted text file

    Returns:
        - This function returns a list containing the line numbers for filtered meteorite data
    '''
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
    '''
    This is the docstring for the line number conditional function
    This function checks which meteorite entries match the user input

    Parameters:
        - data_list contains a line of meteorite data 

        - datachooser contains the index that determines weather mass or year is being looked at

        - fileEntry is an object that contains the user inputted lower bound and upper bound amongst other things

    Returns:
        - This function returns True if the meteorite info matches user input

        - this function returns False if the meteorite data does not match user input or if there is an error
    '''
    try:
        if float(data_list[datachooser]) >= int(fileEntry.lower_bound) and float(data_list[datachooser]) <= int(fileEntry.upper_bound):
            return True
        return False
    except:
        return False

def chooseCategory(datachooser, fileEntry): # picks mass or year category for filter
    '''
    This is the docstring for the choose category function
    This function determines weather mass or year index is used to filter data

    Parameters:
        - datachooser is the variable containing the index that is returned 

        - fileEntry is an object that contains user inputted category amongst other things

    Returns:
        - This function returns the index that determines weather mass or year is filtered
    '''
    datachooser = 0 
    if (fileEntry.titleholder == "MASS"):
        datachooser = 4 
    else:
        datachooser = 6 
    return datachooser
    
def get_all_text_data(line_numbers, header, fileEntry): # gets all the data to write to the new textfile
    '''
    This is the docstring for the get all text data function
    This function opens up the user inputted text file and runs functions that filter and add 
    meteorite data to the text_data list

    Parameters:
        - line_numbers contain the line numbers for where filtered meteorite data is located in the text file

        - header contains the meteorite data headers to be written first to the text file

        - fileEntry is an object that contains the user inputted text file and mode amongst other things

    Returns:
        - This function returns a list text_data that contains all information to be written to the new text file
    '''
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
    '''
    This is the docstring for the add line number function
    This function appends meteorite data to the text_data parameter if the add decider equals True

    Parameters:
        - text_data is a list that contains all data to be written to new text file

        - line contains meteorite data for a single line of the inputted text file 

        - add_decider is a boolean that determines weather the current meteorite entry is appended or not

    Returns:
        - This function does not return
    '''
    if add_decider == True:
        text_data.append(line)

def search_line_numbers(line_numbers, line_counter): # returns true if a line number matches
    '''
    This is the docstring for the search line numbers function
    This function searches the liner_numbers list to see if the current line number (line_counter) is equal to any in the list

    Parameters:
        - line_numbers contains all line numbers that correspond to filtered meteorite entries 

        - line_counter is an integer that represents the current line in the inputted text file being looked at

    Returns:
        - This function returns True is line_counter equals any of the integers in line_numbers list
    '''
    for line_number in line_numbers:
        if line_counter == line_number:
            return True
        else:
            pass

def get_clean_datetime_string():
    '''
    This is the docstring for the get clean date time function
    This function generates the file name for the newly created text file
    The new file name is based off of the current time

    Parameters:
        No Parameters

    Returns:
        - returns a string containing the file name for the newly created text file
    '''
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str
