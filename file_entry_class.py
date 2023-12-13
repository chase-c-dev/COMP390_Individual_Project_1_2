
class FileDataEntry:
    '''
    This is the docstring for the FileDataEntry class
    This class is a FileDataEntry object which contains user input from the prompts

    The user input category this object stores are:
        - titleholder which is year or mass
        
        - lower_bound which is a number that is less than upper bound 
        
        - upper_bound which is a number that is greater than lower bound
        
        - mode which is the mode in which the file will be opened
        
        - textfile which contains the text file path that will be opened
    '''
    titleholder = ''
    lower_bound = ''
    upper_bound = ''
    mode = ''
    textfile = ''

    def __init__(self, titleholder, lower_bound, upper_bound, mode, textfile): # constructor
       '''
       This is the docstring for the __init__ function
       This function intializes the FileDataEntry object with values

       Parameters:
            - titleholder which contains either mass or year

            - lower_bound which contains a number lower than upper bound

            - upper_bound which contain a number greater than lower bound

            - mode which contains the mode in which the text file will be opened ex("r")

            - textfile which contains the file path for the file to be opened
        
        Returns:
            - This function does not return
       '''
       self.titleholder = titleholder
       self.lower_bound = lower_bound
       self.upper_bound = upper_bound
       self.mode = mode
       self.textfile = textfile

    def get_file_info(self): # returns all the information about MeteorDataEntry objects
        '''
        This is the docstring for the get file info function
        This function returns all the information in a FileDataEntry object

        Parameters:
            - self

        Returns:
            returns all the information in a FileDataEntry object
        '''

        return {
            'titleholder': self.titleholder,
            'lower_bound': self.lower_bound,
            'upper_bound': self.upper_bound,
            'mode': self.mode,
            'text_file': self.textfile
        }