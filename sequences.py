def main():
	string = input()
	n0 = n1 = nq = 0
	totalMoves = 0
	for i in range(1, len(string) + 1):
		if string[-i] == '0':
			n0 += 1
			
		elif string[-i] == '1':
			n1 += 1
		else:
			nq += 1


def find(s, ch):
	return [i for i, ltr in enumerate(s) if ltr == ch]

main()