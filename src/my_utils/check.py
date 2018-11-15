import re
from functools import wraps
from .errors import CustomError


"""
Unified check wrapper function

Warning: Do not change the checking order.
"""
def check_wrapper(func):
    @wraps(func)
    def wrapper(record):
        try:
            checkInvalidValueError(record)
            checkOutRangeError(record)
            checkIncorrectFormatError(record)
            checkMazeFormaterror(record)
        except Exception as e:
            print(e)
            exit()
        return func(record)
    return wrapper


"""
Check if the data is out of range
"""
def checkOutRangeError(record):
    (scale, sequence), = record.items()
    # 检查尺寸数字是否超出范围
    for i in str(scale).split(' '):
        if int(i) < 0 :
            raise CustomError("Number out of range.")
    # 检查作图序列数字是否超出范围       
    for i in re.split(r"[;,\s]\s*",str(sequence)):
        if int(i) < 0 :
            raise CustomError("Number out of range.")


"""
Check if the data is valid
"""
def checkInvalidValueError(record):
    (scale, sequence), = record.items()
    for i in str(scale).split(' '):
        if not str.isdigit(i):
            raise CustomError("Invalid number format.")

    for i in re.split(r"[;,\s]\s*",str(sequence)):
        if not str.isdigit(i):
            raise CustomError("Invalid number format.")

"""
Check for formatting errors
"""
def  checkIncorrectFormatError(record):
    (scale, sequence), = record.items()
    scalePattern = re.compile(r"^\d\s\d$")
    sequencePattern = re.compile(r"^\d,\d\s\d,\d$")
    if not scalePattern.match(scale):
        raise CustomError("Incorrect command format.")
    for item in sequence.split(';'):
        if not sequencePattern.match(item):
            raise CustomError("Incorrect command format.​")

"""
Check for connectivity errors
"""
def checkMazeFormaterror(record):
    (scale, sequence), = record.items()
    allNumberChars = re.split(r"[;,\s]\s*",sequence)
    allNumber = [int(a) for a in allNumberChars]
    allCoordinate = [[(allNumber[i],allNumber[i+1]),(allNumber[i+2],allNumber[i+3])] for i in range(0, len(allNumber), 4)]
    for x1, x2 in allCoordinate:
        displacement = [abs(a - b) for a,b in zip(x1,x2)]
        displacement.sort()
        if displacement[-1] > 1 or sum(displacement) > 1:
            raise CustomError("Maze format error.")
    