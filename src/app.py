import re

from .my_utils.check import (
    checkIncorrectFormatError,
    checkInvalidValueError,
    checkMazeFormaterror,
    checkOutRangeError,
    check_wrapper
)


OPERATIONS = {'UP':(-1,0),'DOWN':(1,0),'LEFT':(0,-1),'RIGHT':(0,1)}
WALL_PLACEHOLDER = '[W]'
BLANK_PLACEHOLDER = '[R]'


@check_wrapper
def generateMaze(record):
    (scale, sequence), = record.items()
    scale_temp = scale.split(' ')
    roadGridX = int(scale_temp[0])
    roadGridY = int(scale_temp[1])
    renderGridGraph = initRenderGridGraph(roadGridX, roadGridY)
    steps = initSteps(sequence)
    for step in steps:
        (start_point,operation_str), = step.items()
        y,x = start_point
        renderGridX = 2 * x + 1
        renderGridY = 2 * y + 1 
        operation = OPERATIONS[operation_str]
        middlePointX = renderGridX + operation[1]
        middlePointY = renderGridY + operation[0]
        renderGridGraph[middlePointY][middlePointX] = BLANK_PLACEHOLDER
    return showGraph(renderGridGraph)
    


def initSteps(sequence):
    directions = []
    steps = []
    allNumberChars = re.split(r"[;,\s]\s*",sequence)
    allNumber = [int(a) for a in allNumberChars]
    allCoordinate = [[(allNumber[i],allNumber[i+1]),(allNumber[i+2],allNumber[i+3])] for i in range(0, len(allNumber), 4)]
    for point1, point2 in allCoordinate:
        direction = tuple([b-a for a,b in zip(point1, point2)])
        directions.append(direction)
        reverse_operations = {v:k for k,v in OPERATIONS.items()}
        steps.append({point1:reverse_operations[direction]})
    return steps

'''
initRenderGridGraph: according to roadGridX and roadGridY make a renderGridGraph
'''
def initRenderGridGraph(roadGridX, roadGridY, wallPlaceholder=WALL_PLACEHOLDER,blankPlaceholder=BLANK_PLACEHOLDER):
    renderGridX = 2 * roadGridX + 1
    renderGridY = 2 * roadGridY + 1
    renderGridGraph = makeGraph(renderGridX,renderGridY,placeholder=wallPlaceholder)
    roadGridToRenderGridCoordinates = [(2*y+1, 2*x+1) for x in range(roadGridX) for y in range(roadGridY)]
    for x,y in roadGridToRenderGridCoordinates:
        renderGridGraph[y][x] = blankPlaceholder
    return renderGridGraph


'''
Make a 2D map based on the horizontal coordinate of the incoming ordinate
'''
def makeGraph(x,y,placeholder='0'):
    return [[placeholder for col in range(y)] for row in range(x)]

'''
Elegant output 2D map
'''
def showGraph(mazeGraph):
    graphstrs = []
    for col in mazeGraph:
        for row in col:
            graphstrs.append(str(row) + "\n")
            print(row,end=" ")
        print()
    return graphstrs
