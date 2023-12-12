from terminaltext import *
from file_entry_class import FileDataEntry
import pytest

def createfileEntry():
     fileEntry = FileDataEntry("", "", "", "", "")
     return fileEntry

class Test_Input: # intializes a test input
    def __init__(self, values):
        self.values = iter(values)

    def __call__(self, prompt):
        return next(self.values)
    
# Code to test bounds prompt below
#---------------------------------------------------------------------------------------

def test_bounds_prompt(monkeypatch, capsys): # tests inputting values into bounds prompt
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
    file_entry_test = createfileEntry()
    test_input = Test_Input(["Q", "5"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(SystemExit):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    assert "The program is now exiting Goodbye!" in captured.out

def test_bounds_prompt_None(monkeypatch, capsys): # tests None 
    file_entry_test = createfileEntry()
    test_input = Test_Input([None, None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        bounds_prompt(file_entry_test, "MASS")

    captured = capsys.readouterr()
    assert "INVALID INPUT\n PLEASE ENTER A NUMERIC VALUE" in captured.out

def test_bounds_prompt_real_numbers(monkeypatch, capsys): # tests integers
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
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["learnuseast.txt"])
    monkeypatch.setattr('builtins.input', test_input)

    file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "Target file: learnuseast.txt" in captured.out
    assert file_entry_test.textfile == 'learnuseast.txt'

def test_filepath_prompt_letters(monkeypatch, capsys): # tests with random letters inputted
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["gdiudwb"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_numbers(monkeypatch, capsys): # tests numbers inputted
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input([0])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_wrongpath(monkeypatch, capsys): # tests with wrong file path inputted
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input(["learnusseast.txt"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_None(monkeypatch, capsys): # tests with wrong file path inputted
    file_entry_test = createfileEntry()
    prompt = "Enter a valid file name(ex. filename.txt) with its file extension (if applicable) or enter >q or >Q to quit"

    test_input = Test_Input([None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_path_data_prompter(file_entry_test, prompt, "Target file: ")

    captured = capsys.readouterr()
    assert "INVALID FILE PATH\n Please Try Again\n" in captured.out

def test_filepath_prompt_exit(monkeypatch, capsys): # tests with wrong file path inputted
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
    file_entry_test = createfileEntry()

    test_input = Test_Input(["r"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert file_entry_test.mode == 'r'

def test_mode_prompt_write(monkeypatch, capsys): # tests with normal file mode
    file_entry_test = createfileEntry()

    test_input = Test_Input(["w"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert file_entry_test.mode == 'w'

def test_mode_prompt_letters(monkeypatch, capsys): # tests with to many letters
    file_entry_test = createfileEntry()

    test_input = Test_Input(["rrr"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_numbers(monkeypatch, capsys): # tests with to many letters
    file_entry_test = createfileEntry()

    test_input = Test_Input(["423645"])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_none(monkeypatch, capsys): # tests with to many letters
    file_entry_test = createfileEntry()

    test_input = Test_Input([None])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out

def test_mode_prompt_numbers(monkeypatch, capsys): # tests with to many letters
    file_entry_test = createfileEntry()

    test_input = Test_Input([0])
    monkeypatch.setattr('builtins.input', test_input)

    with pytest.raises(StopIteration):
        file_mode_data_prompter(file_entry_test, mode_prompt_return(), "File Mode: ")

    captured = capsys.readouterr()
    assert "INVALID FILE MODE\n Please Try Again\n" in captured.out