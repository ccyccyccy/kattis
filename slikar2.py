def main():
	size = int(input())
	lines = []
	for i in range(size):
		line = input()
		lines.append(line)
	# lines[y][x] is pixel on y row and x col
	min, path = magicCost(lines, size)
	print(min)
	result = (magic(lines, size, path))
	for line in result:
		print(line)

def magic(lines, size, path):
	if size == 2:
		if path[0] < 2: # If 0-1 index is less than 2, means is the top part
			lines[0] = replace(lines[0], index=path[0], replacement='1')
		else:
			lines[1] = replace(lines[1], index=path[0] - 2, replacement='1')
		if path[1] < 2:
			lines[0] = replace(lines[0], index=path[1], replacement='0')
		else:
			lines[1] = replace(lines[1], index=path[1] - 2, replacement='0')
		return lines

	smallsquares = splitSquare(lines, size)
	smallsquares[path[0]] = to1(size/2)
	smallsquares[path[1]] = to0(size/2)
	otherNum = [0,1,2,3]
	otherNum.remove(path[0])
	otherNum.remove(path[1])

	for i in range(2):
		smallsquares[otherNum[i]] = magic(smallsquares[otherNum[i]], size / 2, path[i+2])

	return joinSquares(smallsquares)



def magicCost(lines, size): # Returns cost, pathToSquare
	if size == 1: # If it is 1 pixel, cost = 0
		return [0, None]
	smallsquares = splitSquare(lines, size)
	smallsquarescosts = [] # 0-1 cost, 1-0 cost, magicCost
	for square in smallsquares:
		zt1cost = 0
		ot0cost = 0
		for line in square:
			zt1cost += line.count('0')
		ot0cost = int(size**2 / 4 - zt1cost)
		magCost, pathToSmallerSquare = magicCost(square, int(size/2))
		smallsquarescosts.append([zt1cost, ot0cost, magCost, pathToSmallerSquare])

	minCost = 10e9
	for i in range(4): # Choose 1 to be 0-1	
		for j in range(4): # Choose 1 to be 1-0
			cost = smallsquarescosts[i][0]
			if j == i:
				continue
			cost += smallsquarescosts[j][1]
			for k in range(4): # The rest be magCost
				if k == j or k == i:
					continue
				cost += smallsquarescosts[k][2]
			if cost < minCost:
				minCost = cost
				minList = [i,j] # smallsquare[i] 0-1, smallsquare[j] 1-0

	minI = minList[0]
	minJ = minList[1]
	otherNum = []
	for i in range(4):
		if i == minI or i == minJ:
			continue
		otherNum.append(i)
	return [minCost, [minI, minJ, smallsquarescosts[otherNum[0]][3], smallsquarescosts[otherNum[1]][3]]]



def splitSquare(lines, bigsize): # Returns topleft, topright, botleft, botright
	smallsize = int(bigsize/2)
	topleft = [x[:smallsize] for x in lines[:smallsize]]
	topright = [x[smallsize:] for x in lines[:smallsize]]
	botleft = [x[:smallsize] for x in lines[smallsize:]]
	botright = [x[smallsize:] for x in lines[smallsize:]]
	return [topleft, topright, botleft, botright]

def joinSquares(squares):
	out = []
	for leftline, rightline in zip(squares[0], squares[1]):
		out.append(leftline + rightline)
	for leftline, rightline in zip(squares[2], squares[3]):
		out.append(leftline + rightline)
	return out

def replace(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def to0(size):
	size = int(size)
	return ['0' * size] * size

def to1(size):
	size = int(size)
	return ['1' * size] * size

main()