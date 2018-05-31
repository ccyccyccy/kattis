numberOfQuestions = int(input())
for i in range(numberOfQuestions):
	line = input()
	if(line.startswith('Simon says')):
		print(line[11:])