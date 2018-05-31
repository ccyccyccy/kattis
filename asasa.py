def main():
	line = input().split(' ')
	ndict = int(line[0])
	name = line[1]
	dict = []
	for i in range(ndict):
		dict.append(input().split(' '))
	for d in dict:
		d[1] = int(d[1])

	print(compare(name, dict))


def compare(fragment, cmpdict): # Returns multiplier of fragment
	multiplier = 0
	for word in cmpdict:
		if word[0] in fragment:
			print(word[0] + ' is in ' + fragment)
			wordleft = fragment[:fragment.find(word[0])]
			wordright = fragment[fragment.find(word[0]) + len(word[0]):]
			if len(wordleft) == len(wordright) == 0:
				multiplier += word[1]
			elif len(wordleft) != 0 and len(wordright) != 0:
				multiplier += word[1] * compare(wordleft, cmpdict[cmpdict.index(word) + 1:]) * compare(wordright, cmpdict[cmpdict.index(word) + 1:])
			elif len(wordleft) != 0:
				multiplier += word[1] * compare(wordleft, cmpdict[cmpdict.index(word) + 1:])
			elif len(wordright) != 0:
				multiplier += word[1] * compare(wordright, cmpdict[cmpdict.index(word) + 1:])

	print('Final Multiplier for ' + fragment + ' is ' + str(multiplier))

	return multiplier

main()
