from terminaltext import *
from file_entry_class import FileDataEntry
import pytest

def createfileEntry():
    '''
    This is the docstring for the create file entry function
    This function creates a new file entry object

    Parameters:
        No Parameters

    Returns:
        - returns file entry object
    '''
    fileEntry = FileDataEntry("", "", "", "", "")
    return fileEntry

class Test_Input: # intializes a test input
    '''
    This is the docstring for the test input class
    This class has two functions that intialize and call test inputs for unit testing

    Parameters:
        - values is the input values that are utilized in the functions

    Returns:
        - call returns the value that was inputted into the class
    '''
    def __init__(self, values):
        self.values = iter(values)

    def __call__(self, prompt):
        return next(self.values)
    
# Code to test bounds prompt below
#---------------------------------------------------------------------------------------

def test_bounds_prompt(monkeypatch, capsys): # tests inputting values into bounds prompt
    '''
    This is the docstring for the test bounds prompt function
    This function is a unit test for the bounds prompt function and tests for 
    correct user input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input1 = Test_Input(["2", "5"])
    monkeypatch.setattr('builtins.input', test_input1)

    bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    # test for normal conditions
    assert "Lower Bound: 2" in captured.out
    assert "Upper Bound: 5" in captured.out
    assert file_entry_test.lower_bound == '2'
    assert file_entry_test.upper_bound == '5'

# tests for lower bound greater then upper bound
# tests to see if program reprompts when the lower bound is greater than the upper
def test_bounds_prompt_greater_than_error(monkeypatch, capsys): 
    '''
    This is the docstring for the test bounds greater than error function
    This function is a unit test for the bounds prompt function that tests when lower bound
    inputted is greater than upper bound

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    test_input = Test_Input(["7", "3"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    # test for bounds not lining up
    assert "Lower Bound: 7" in captured.out
    assert "Upper Bound: 3" in captured.out
    assert file_entry_test.lower_bound == '7'
    assert file_entry_test.upper_bound == '3'

# tests for bound being alphabetic
def test_bounds_prompt_non_number_error(monkeypatch, capsys): 
    '''
    This is the docstring for the test bounds prompt non number function
    This function is a unit test for the bounds prompt function that tests when the user
    inputs letters instead of numbers

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    test_input = Test_Input(["abc", "xyz"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()

    #print("Captured Output:", captured.out)

    # Test for bounds not lining up and error message
    assert "Lower Bound: abc" in captured.out
    assert "INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE" in captured.out

def test_bounds_prompt_zero(monkeypatch, capsys): # tests inputting zero into bounds prompt
    '''
    This is the docstring for the test bounds prompt zero function
    This function is a unit test for the bounds prompt function tests for when the user inputs
    0 for lower bound and 10 for upper bound

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input1 = Test_Input(["0", "10"])
    monkeypatch.setattr('builtins.input', test_input1)

    bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    # test for normal conditions
    assert "Lower Bound: 0" in captured.out
    assert "Upper Bound: 10" in captured.out
    assert file_entry_test.lower_bound == '0'
    assert file_entry_test.upper_bound == '10'

def test_bounds_prompt_quit(monkeypatch, capsys): # tests the quit (Q) for bounds prompt
    '''
    This is the docstring for the test bounds prompt quit function
    This function is a unit test for the bounds prompt function and tests to make
    sure the function quits 

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    test_input = Test_Input(["Q", "5"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(SystemExit):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    assert "The program is now exiting Goodbye!" in captured.out

def test_bounds_prompt_None(monkeypatch, capsys): # tests None 
    '''
    This is the docstring for the test bounds prompt None function
    This function is a unit test for the bounds prompt function and tests for
    a None input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    test_input = Test_Input([None, None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    assert "INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE" in captured.out

def test_bounds_prompt_real_numbers(monkeypatch, capsys): # tests integers
    '''
    This is the docstring for the test bounds prompt real numbers function
    This function is a unit test for the bounds prompt function and tests for
    integer input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    test_input = Test_Input([0, 0])
    monkeypatch.setattr('builtins.input', test_input)

    #with pytest.raises(StopIteration):
    bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    assert file_entry_test.lower_bound == 0
    assert file_entry_test.upper_bound == 0

# Code to test file path function below
#------------------------------------------------------------------------------------------------

def test_filepath_prompt(monkeypatch, capsys): # tests with normal file path
    '''
    This is the docstring for the test file path prompt function
    This function is a unit test for the file path data prompt function and tests for
    a correct user input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["learnuseast.txt"])
    monkeypatch.setattr('builtins.input', test_input)

    file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "Target file: learnuseast.txt" in captured.out
    assert file_entry_test.textfile == 'learnuseast.txt'

def test_filepath_prompt_letters(monkeypatch, capsys): # tests with random letters inputted
    '''
    This is the docstring for the file path letters prompt function
    This function is a unit test for the file path data prompt function and tests for letters
    input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["gdiudwb"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_numbers(monkeypatch, capsys): # tests numbers inputted
    '''
    This is the docstring for the file path prompt numbers function
    This function is a unit test for the file path data prompt function and tests for an integer input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input([0])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_wrongpath(monkeypatch, capsys): # tests with wrong file path inputted
    '''
    This is the docstring for the test file path prompt wrong path function
    This function is a unit test for the file path data prompt function and tests for
    an incorrect file path

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["learnusseast.txt"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_None(monkeypatch, capsys): # tests with wrong file path inputted
    '''
    This is the docstring for test file path prompt None function 
    This function is a unit test for the file path data prompt function and tests for a None input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input([None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_exit(monkeypatch, capsys): # tests with wrong file path inputted
    '''
    This is the docstring for the test file path prompt exit function
    This function is a unit test for the file path data prompt function and tests for when a user
    quits the program

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input([">q"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(SystemExit):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "The program is now exiting Goodbye!" in captured.out

# Code to test mode prompt function below
#------------------------------------------------------------------------------------------------

def mode_prompt_return():
    '''
    This is the docstring for the mode prompt return function
    This function returns the prompt for mode input

    Parameters:
        No Parameters

    Returns:
        - This function returns mode_prompt which contains the string for the mode prompt
    '''
    mode_prompt = '"r" - open for reading (default)\n'
    '"m" - open for writing, truncating the file first (WARNING: this mode will delete the contents of an existing file)\n'
    '"x" - open for exclusive creation, failing if the file already exists\n'
    '"a" - open for writing, appending to the end of file if it exists\n'
    '"b" - binary mode\n'
    '"t" - text mode(default)\n'
    '"+" - open for updating (reading and writing)\n'
    "Enter >q or >Q to quit\n", "File Mode: "
    return mode_prompt

def test_mode_prompt(monkeypatch, capsys): # tests with normal file mode
    '''
    This is the docstring for the test mode prompt function 
    This function is a unit test for the file mode data prompter function that tests for correct user input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input(["r"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert file_entry_test.mode == 'r'

def test_mode_prompt_write(monkeypatch, capsys): # tests with normal file mode
    '''
    This is the docstring for the test mode prompt write function
    This function is a unit test for the file mode data prompter function that tests for a "w" write input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input(["w"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert file_entry_test.mode == 'w'

def test_mode_prompt_letters(monkeypatch, capsys): # tests with to many letters
    '''
    This is the docstring for the test mode prompt letters function
    This function is a unit test for the file mode data prompter function that tests for
    when letters are inputted

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input(["rrr"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_numbers(monkeypatch, capsys): # tests with to many letters
    '''
    This is the docstring for the test mode prompt numbers function
    This function is a unit test for the file mode data prompter function that tests for when
    the user inputs numbers

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input(["423645"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_none(monkeypatch, capsys): # tests with to many letters
    '''
    This is the docstring for the test mode prompt none function
    This function is a unit test for the file mode data prompter function that tests for when
    the input is None

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input([None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_integers(monkeypatch, capsys): # tests with to many letters
    '''
    This is the docstring for the test mode prompt numbers function
    This function is a unit test for the file mode data prompter function that tests for integer input

    Parameters:
        - monkeypatch provides methods that are useful for modifying functions, classes or objects during testing

        - capsys allows you to inspect output and error during a test

    Returns:
        - This function does not return
    '''
    file_entry_test = createfileEntry()

    test_input = Test_Input([0])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out