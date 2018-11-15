import pytest
from src.app import generateMaze
from src.my_utils.errors import CustomError
from src.my_utils.check import (
    checkIncorrectFormatError,
    checkInvalidValueError,
    checkMazeFormaterror,
    checkOutRangeError,
)

def test_normal():
    recordNormal = {"3 3":"0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"}
    # recordNormal = {"3 3":"0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1"}
    result = checkIncorrectFormatError(recordNormal)
    assert result == None
    result = checkInvalidValueError(recordNormal)
    assert result == None
    result = checkMazeFormaterror(recordNormal)
    assert result == None
    result = checkOutRangeError(recordNormal)
    assert result == None

def test_InvalidValueError():
    recordInvalidValueError = {"b 3":"0,1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkInvalidValueError(recordInvalidValueError)
    assert "Invalid number format." == str(excinfo.value)
    recordInvalidValueError = {"3 3":",1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkInvalidValueError(recordInvalidValueError)
    assert "Invalid number format." == str(excinfo.value)
    recordInvalidValueError = {"3 3":"0,1 0,2;u,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkInvalidValueError(recordInvalidValueError)
    assert "Invalid number format." == str(excinfo.value)

def test_IncorrectFormatError():
    record = {"3 3 4 5":"0,1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkIncorrectFormatError(record)
    assert "Incorrect" in str(excinfo.value)
    record = {"3 3":"0,1 0,2;0,0 1,0;0,3"}
    with pytest.raises(Exception) as excinfo:
        checkIncorrectFormatError(record)
    assert "Incorrect" in str(excinfo.value)

def test_OutRangeError():
    record = {"3 -3":"0,1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkOutRangeError(record)
    assert "out of" in str(excinfo.value)
    record = {"3 3":"0,-1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkOutRangeError(record)
    assert "out of" in str(excinfo.value)

def test_MazeFormaterror():
    record = {"3 3":"1,1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkMazeFormaterror(record)
    assert "format" in str(excinfo.value)
    record = {"3 3":"3,1 0,2;0,0 1,0"}
    with pytest.raises(Exception) as excinfo:
        checkMazeFormaterror(record)
    assert "format" in str(excinfo.value)    