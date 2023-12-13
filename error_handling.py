def check_file_path(fileEntry, output_text): # checks for errors in file path
    '''
    This is the docstring for the check file path function
    this function error checks the file name prompt to ensure there was correct input

    Parameters:
        - fileEntry is an object that contains the user inputted file name amongst other things

        - output_text is a string that contains the text to be attached to the user input to let them know
          what they inputted for the prompt

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        with open(fileEntry.textfile, "r") as f:
            pass
        print("\n" + output_text + fileEntry.textfile + "\n")
        return True
    except:
        print("INVALID FILE PATH\n Please Try Again\n")
        return False
    
def check_for_mode(fileEntry, output_text): # checks for errors in mode
    '''
    This is the docstring for the check for mode function
    this function error checks the mode prompt for user input

    Parameters:
        - fileEntry is an object that contains the user inputted file name and mode amongst other things

        - output_text is a string that contains the text to be attached to the user input to let them know
          what they inputted for the prompt

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        with open(fileEntry.textfile, fileEntry.mode) as f:
            pass
        print("\n" + output_text + fileEntry.mode + "\n")
        return True
    except:
        print("INVALID FILE MODE\n Please Try Again\n")
        return False
    
def filter_category_check(output_text): # checks for errors in choosing data filter type
    '''
    This is the docstring for the filter category check function
    this function error checks the choose a category to filter by prompt to ensure correct user input

    Parameters:
        - output_text is a string that contains the text to be attached to the user input to let them know
          what they inputted for the prompt

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        if (int(output_text) > 0 and int(output_text) < 4):
            return True
        else:
            print("INVALID INPUT\n PLEASE ENTER NUMBER 1 through 3 BASED ON OPTIONS PROMPT\n")
            return False
    except:
        print("INVALID INPUT\n PLEASE ENTER NUMBER 1 through 3 BASED ON OPTIONS PROMPT\n")
        return False
    
def check_lower_bound(fileEntry, label_text): # checks for errors in lower bound user input
    '''
    This is the docstring for the check lower bound function
    This function error checks lower bound prompt for user input

    Parameters:
        - fileEntry is an object that contains the user inputted lower bound amongst other things

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        check = int(fileEntry.lower_bound)
        return True
    except:
        print("INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE")
        return False

def check_upper_bound(fileEntry, label_text): # checks for errors in upper bound user input
    '''
    This is the docstring for the check upper bound function
    this function error checks the upper bound prompt for user input

    Parameters:
        - fileEntry is an object that contains the user inputted upper bound amongst other things

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        if int(fileEntry.lower_bound) > int(fileEntry.upper_bound):
            print("INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE THAT IS GREATER THAN THE LOWER BOUND")
            return False
        check = int(fileEntry.upper_bound)
        return True
    except:
        print("INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE THAT IS GREATER THAN THE LOWER BOUND")
        return False
    
def check_display_type(output_type, fileEntry): # error checking for display type
    '''
    This is the docstring for the check display type function
    This function error checks the prompt for how the user wants the results to be displayed to ensure
    correct user input

    Parameters:
        - fileEntry is an object that contains user inputted elements

        - output_text is a string that contains the text to be attached to the user input to let them know
          what they inputted for the prompt

    Returns:
        - This function returns True is user input is correct and False if it is not
    '''
    try:
        if int(output_type) > 0 and int(output_type) < 5:
            return True
        print("INVALID INPUT\n ENTER A NUMBER 1 THROUGH 4 BASED ON OPTIONS PROVIDED")
        return False
    except:
        print("INVALID INPUT\n ENTER A NUMBER 1 THROUGH 4 BASED ON OPTIONS PROVIDED")
        return False
        
