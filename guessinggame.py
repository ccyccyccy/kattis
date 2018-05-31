def startGame():
	resp = ''
	for i in range(2500):
		possibleAnswers = [1] * 11
		while True:
			guess = int(input())
			if resp == 'right on' and guess == 0:
				return;
			resp = input()
			if resp == 'right on':
				if possibleAnswers[guess] == 0:
					print('Stan is dishonest')
				else:
					print('Stan may be honest')
				break
			elif resp == 'too high':
				for i in range(guess, len(possibleAnswers)):
					possibleAnswers[i] = 0
			elif resp == 'too low':
				for i in range(guess+1):
					possibleAnswers[i] = 0

startGame()