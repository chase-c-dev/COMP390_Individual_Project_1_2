def check_file_path(fileEntry, output_text): # checks for errors in file path
    try:
        with open(fileEntry.textfile, "r") as f:
            pass
        print("\n" + output_text + fileEntry.textfile + "\n")
        return True
    except:
        print("INVALID FILE PATH\n Please Try Again\n")
        return False
    
def check_for_mode(fileEntry, output_text): # checks for errors in mode
    try:
        with open(fileEntry.textfile, fileEntry.mode) as f:
            pass
        print("\n" + output_text + fileEntry.mode + "\n")
        return True
    except:
        print("INVALID FILE MODE\n Please Try Again\n")
        return False
    
def filter_category_check(output_text): # checks for errors in choosing data filter type
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
    try:
        check = int(fileEntry.lower_bound)
        return True
    except:
        print("INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE")
        return False

def check_upper_bound(fileEntry, label_text): # checks for errors in upper bound user input
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
    try:
        if int(output_type) > 0 and int(output_type) < 5:
            return True
        print("INVALID INPUT\n ENTER A NUMBER 1 THROUGH 4 BASED ON OPTIONS PROVIDED")
        return False
    except:
        print("INVALID INPUT\n ENTER A NUMBER 1 THROUGH 4 BASED ON OPTIONS PROVIDED")
        return False
        
