def hasLowerAdjacentCell(x, y):
    # Returns True if there is an adjacent cell with lower level than it
    # Else returns False
    currentValue = terrace[y][x]
    returnValue = False
    if y < len(terrace) - 1:
        if terrace[y + 1][x] < currentValue:
            returnValue = True
    if y != 0:
        if terrace[y - 1][x] < currentValue:
            returnValue = True
    if x < len(terrace[y]) - 1:
        if terrace[y][x + 1] < currentValue:
            returnValue = True
    if x != 0:
        if terrace[y][x - 1] < currentValue:
            returnValue = True
    return returnValue


def cascadeEffect(x, y):
    currentValue = terrace[y][x]
    if y < len(terrace) - 1:
        if terrace[y + 1][x] >= currentValue and isFlooded[y + 1][x] == 1:
            isFlooded[y + 1][x] = 0
            cascadeEffect(x, y + 1)
    if y != 0:
        if terrace[y - 1][x] >= currentValue and isFlooded[y - 1][x] == 1:
            isFlooded[y - 1][x] = 0
            cascadeEffect(x, y - 1)
    if x < len(terrace[y]) - 1:
        if terrace[y][x + 1] >= currentValue and isFlooded[y][x + 1] == 1:
            isFlooded[y][x + 1] = 0
            cascadeEffect(x + 1, y)
    if x != 0:
        if terrace[y][x - 1] >= currentValue and isFlooded[y][x - 1] == 1:
            isFlooded[y][x - 1] = 0
            cascadeEffect(x - 1, y)


'''
Check order: Top to bottom, left to right
set all cells to flood cells at first
check all invididual cells at least once
if one cell fails, check all adjacent cells if they are the same level,
	cascading the failure to all the cells
'''
import sys
sys.setrecursionlimit(100000)
x, y = input().split(' ')
x = int(x)
y = int(y)
if x <= 0:
	exit()
if y <= 0:
	exit()
terrace = []
isFlooded = [[1] * x for i in range(y)]
for i in range(y):
    terrace.append([int(j) for j in input().split(' ')])
for i in range(y):
    for j in range(x):
        if isFlooded[i][j] == 0:
            continue
        if hasLowerAdjacentCell(j, i):
            isFlooded[i][j] = 0
            cascadeEffect(j, i)
final = 0
for i in range(len(isFlooded)):
    final += sum(isFlooded[i])
print(final)