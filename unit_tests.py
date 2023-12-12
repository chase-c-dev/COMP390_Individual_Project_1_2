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

    print("Captured Output:", captured.out)

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