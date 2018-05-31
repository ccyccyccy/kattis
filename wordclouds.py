n, maxWidth = map(int, input().split(' '))
blockList = []
for i in range(n):
	blockList.append(list(map(int, input().split(' ')))) # Width, Height
minHeightList = [0] * n
minHeightList[0] = blockList[0][1]
for i in range(n):
	curWidth = blockList[i][0]
	maxHeight = blockList[i][1]
	for j in range(i - 1, -1, -1):
		curWidth += blockList[j][0]
		if curWidth > maxWidth:
			minHeightList[i] = maxHeight + minHeightList[j]
			break
		maxHeight = max(maxHeight, blockList[j][1])
		minHeightList[i] = maxHeight
print(minHeightList[n-1])
