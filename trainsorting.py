numberOfTrain = int(input())

weights = []
for i in range(numberOfTrain):
	weights.append(int(input()))

groups []
i = 0
while True:
	while True:
		upperBound = max(weights[i], weights[i+1], weights[i+2])
		lowerBound = min(weights[i], weights[i+1], weights[i+2])
		i += 3
		