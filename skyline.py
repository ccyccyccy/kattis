def main():
	numberOfBuildings = int(input())
	buildings = []
	for i in range(numberOfBuildings):
		building = Building([int(j) for j in input().split(' ')])
		buildings.append(building)
	for i in range(numberOfBuildings):
		overlapAreaPercentage = 1
		currentBuildingArea = buildings[i].area()
		buildingsInInterval = [build for build in buildings[:i] if not (build.x2 < buildings[i].x1 or build.x1 > buildings[i].x2)]
		if len(buildingsInInterval) == 0:
			print(1)
			continue
		# Initialize starting
		startX = buildings[i].x1
		currentX = startX
		buildToCompare = [build for build in buildingsInInterval if build.has(startX)]
		buildToCompare.sort(key=lambda x: x.findyatx(startX)) # What if 2 buildings has same height? Higher gradiant win
		if len(buildToCompare) == 0:
			currentTallestCoveringBuilding = None
		else:
			currentTallestCoveringBuilding = buildToCompare[-1]
		# Find next intersect / next new appearance. Check new appearance. Switch if intersect
		# List all new appearance
		notableAppearances = [build for build in buildingsInInterval if build.x1 > startX]
		notableAppearances.sort(key = lambda x: x.x1)

		while currentX < buildings[i].x2:
		# List all intersects with respect to current tallest building
			if currentTallestCoveringBuilding == None:
				buildToComparee = [build for build in buildingsInInterval if build.has(currentX+0.00000001)]
				buildToComparee.sort(key=lambda x: x.findyatx(startX))
				if(len(buildToComparee) != 0):
					currentTallestCoveringBuilding = buildToComparee[0]
					continue
				# Just use next appearance
				if len(notableAppearances) == 0:
					break
				currentTallestCoveringBuilding = notableAppearances[0]
				currentX = currentTallestCoveringBuilding.x1
				continue
				
			else:
				intersectList = [] # List of tuples containing (Building, intersectX)
				for build in buildingsInInterval:
					# Check if they intersect within the interval, record down the x axis if it does
					intersect = currentTallestCoveringBuilding.intersectAt(build)
					if intersect <= currentX or intersect >= currentTallestCoveringBuilding.x2 or intersect <= currentTallestCoveringBuilding.x1:
						continue
					else:
						intersectList.append((build, intersect))
			
			if len(intersectList) == 0:
				# Find overlap area to the end of the line segment
				overlapArea = overlap(buildings[i], currentTallestCoveringBuilding, currentX, min(buildings[i].x2, currentTallestCoveringBuilding.x2))
				# Set current X to the end of line segment
				currentX = currentTallestCoveringBuilding.x2
				# Set currentTallestCoveringBuilding = None
				currentTallestCoveringBuilding = None
				# Minus overlapping percentage
				overlapAreaPercentage -= overlapArea / buildings[i].area()
				

			else:
				intersectList.sort(key=lambda x: x[1])
				# Find overlap area to the intersect
				overlapArea = overlap(buildings[i], currentTallestCoveringBuilding, currentX, intersectList[0][1])
				# Set current X to intersect
				currentX = intersectList[0][1]
				# Set currentTallestCoveringBuilding = newBuilding
				currentTallestCoveringBuilding = intersectList[0][0]
				# Minus overlapping percentage
				overlapAreaPercentage -= overlapArea / buildings[i].area()
			# Trim notableAppearances
			for m in notableAppearances:
				if m.x1 < currentX:
					notableAppearances.remove(m)
		print(overlapAreaPercentage)


'''
calculate highest line at the start
check it's next intersection with any lines, and check next new line segments appearance
compare which is higher
if not higher, continue to check next, else calculate area overlap, continue with new line
'''
class Building:
	def __init__(self, numbers):
		# TAKE NOTE IF BUILDING IS ZERO WIDTH, CANNOT DIVIDE BY 0
		self.x1, self.y1, self.x2, self.y2 = numbers
		self.grad = (self.y1-self.y2)/(self.x1-self.x2)
		self.c = self.y1 - self.grad*self.x1

	def findyatx(self, xx):
		return self.grad*xx + self.c

	def area(self):
		return abs(self.x1 - self.x2) * (self.y1+self.y2) / 2

	def has(self, x):
		return x < self.x2 and x > self.x1

	def intersectAt(self, building):
		if self.grad == building.grad:
			return -1
		return (self.c - building.c) / (building.grad - self.grad)


def overlap(b1, b2, x1, x2): # Returns area of intersect
	if b1.x2 < b2.x1 or b2.x2 < b1.x1: # Not overlapping
		print('Error! Tried to find overlap between 2 non-overlapping buildings')
		return 0
	intersect = True
	if b1.grad == b2.grad:
		intersect = False
	else:
		intersectx = b2.intersectAt(b1)
		if intersectx < x1 or intersectx > x2:
			intersect = False
	if intersect:
		intersecty = b1.findyatx(intersectx)
		if(b1.grad > b2.grad): # Was lower before intersect
			return (intersectx - x1) * (intersecty + b1.findyatx(x1))/2 + (x2 - intersectx) * (b2.findyatx(x2) + intersecty) / 2
		else:
			return (intersectx - x1) * (intersecty + b2.findyatx(x1))/2 + (x2 - intersectx) * (b1.findyatx(x2) + intersecty) / 2
	else:
		height1 = b1.findyatx(x1)
		height2 = b2.findyatx(x1)
		if height1 < height2:
			return (height1 + b1.findyatx(x2))/2 * (x2-x1)
		else:
			return (height2 + b2.findyatx(x2))/2 * (x2-x1)

def intersectX(b1, b2): # Returns intersextX or False if outside interval
	interval = [max(b1.x1, b2.x1) ,min(b1.x2, b2.x2)]
	if b1.grad == b2.grad:
		intersectx = False
	else:
		intersectx = (b2.c - b1.c) / (b1.grad - b2.grad)
		if intersectx < x1 or intersectx > x2:
			intersectx = False
	return intersectx

main()
