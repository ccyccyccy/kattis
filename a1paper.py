def main():
	smallest = input()
	numbers = input().split(' ')
	numbers = [int(number) for number in numbers]
	stop = 0
	totalArea = 0
	for i in range(len(numbers)):
		totalArea += numbers[i] / (2**(i+1))
		if totalArea >= 1:
			stop = i
			break
	if totalArea < 1:
		print('impossible')
		return
	totalLength = 0
	totalArea = 0
	for i in range(stop):
		totalArea += numbers[i] / (2**(i+1))
	numberOfSmallest = (1-totalArea) * (2**(stop+1))
	numbers[stop] = numberOfSmallest
	for i in range(stop, -1, -1):
		totalLength += lengthForIndex(i) * numbers[i] / 2
		numbers[i-1] += numbers[i] / 2
	print(totalLength)



def lengthForIndex(i):
	return 2**(-3/4 - i/2)

main()