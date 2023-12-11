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
        
