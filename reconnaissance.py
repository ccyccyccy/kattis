def main():
	nlines = int(input())
	lines = []
	for i in range(nlines):
		lines.append(list(map(int, input().split(' ')))) # c, grad

	tallest = max(lines, key=lambda x: (x[0], x[1])) # max at t=0, if same, choose highest grad
	shortest = min(lines, key=lambda x: (x[0], x[1])) # min at t=0, if same, choose lowest grad

	currentX = 0
	shortestRange = distanceAtX(0, tallest, shortest)

	while True: # WHAT IF THERE IS DUPLICATE LINES? WHAT IF THEY INTERSECT AT THE SAME POINT?
		linesExceptTallest = list(lines)
		linesExceptTallest.remove(tallest)
		linesExceptShortest = list(lines)
		linesExceptShortest.remove(shortest)
		# Order: Intersect, line
		nextTallestXIntersect = 10e9
		nextTallestLine = None
		for line in linesExceptTallest:
			if tallest[1] - line[1] != 0:
				inter = (line[0] - tallest[0]) / (tallest[1] - line[1])
				if inter < nextTallestXIntersect and inter > currentX:
					nextTallestXIntersect = inter
					nextTallestLine = line
				elif inter == nextTallestXIntersect and inter > currentX and line[1] > nextTallestLine[1]:
					nextTallestLine = line

		nextShortestXIntersect = 10e9
		nextShortestLine = None
		for line in linesExceptShortest:
			if shortest[1] - line[1] != 0:
				inter = (line[0] - shortest[0]) / (shortest[1] - line[1])
				if inter < nextShortestXIntersect and inter > currentX:
					nextShortestXIntersect = inter
					nextShortestLine = line
				elif inter == nextShortestXIntersect and inter > currentX and line[1] < nextShortestLine[1]:
					nextShortestLine = line

		if nextTallestLine == nextShortestLine == None:
			break
		if nextShortestLine == None:
			intersect = nextTallestXIntersect
		elif nextTallestLine == None:
			intersect = nextShortestXIntersect
		else:
			intersect = min(nextTallestXIntersect, nextShortestXIntersect)
		shortestRange = min(distanceAtX(currentX, tallest, shortest), distanceAtX(intersect, tallest, shortest), shortestRange)
		currentX = intersect
		if nextTallestXIntersect < nextShortestXIntersect:
			tallest = nextTallestLine
		else:
			shortest = nextShortestLine

	print(shortestRange)

def distanceAtX(x, line1, line2):
	return abs(line1[1] * x + line1[0] - line2[1] * x - line2[0])

main()