n = int(input())
pairs = []
for i in range(5):
	string = input()
	nphotos = int(string[0])
	for j in range(nphotos):
		pair = list(map(int, string[3+5*j:3+5*j+3].split(' ')))
		pairs.append(pair)
# Default is A
for pair in pairs:
	pair.sort()
pairs.sort(key=lambda x: x[0])
