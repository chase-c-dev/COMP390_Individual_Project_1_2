class FileDataEntry:
    titleholder = ''
    lower_bound = ''
    upper_bound = ''
    mode = ''
    textfile = ''

    def __init__(self, titleholder, lower_bound, upper_bound, mode, textfile): # constructor
       self.titleholder = titleholder
       self.lower_bound = lower_bound
       self.upper_bound = upper_bound
       self.mode = mode
       self.textfile = textfile

    def get_file_info(self): # returns all the information about MeteorDataEntry objects
            return {
                'titleholder': self.titleholder,
                'lower_bound': self.lower_bound,
                'upper_bound': self.upper_bound,
                'mode': self.mode,
                'text_file': self.textfile
            }