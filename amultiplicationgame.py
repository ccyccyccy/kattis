from math import ceil

inputs = []
'''
while True:
	try:
		line = input()
	except EOFError:
		break
	inputs.append(line)
for i in range(len(inputs)):
	n = int(inputs[i])
'''

while True:
	n = int(input())
	n = ceil(n / 9)
	eo = 0
	while n <= 9 and n >= 2:
		n = ceil(n / 2)
		eo += 1

	if eo % 2 == 0:
		print('Stan wins.')
	else:
		print('Ollie wins.')