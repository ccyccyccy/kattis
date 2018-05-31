def main():
	wtcj = 'welcome to code jam'
	n = int(input())
	for i in range(n):
		sentence = input()
		allw = find(sentence, 'w')
		alle = find(sentence, 'e')
		alll = find(sentence, 'l')
		allc = find(sentence, 'c')
		allo = find(sentence, 'o')
		allm = find(sentence, 'm')
		allsp = find(sentence, ' ')
		allt = find(sentence, 't')
		alld = find(sentence, 'd')
		allj = find(sentence, 'j')
		alla = find(sentence, 'a')
		allm = find(sentence, 'm')
		allindex = [allw, alle, alll, allc, allo, allm, alle, allsp, allt, allo,
		allsp, allc, allo, alld, alle, allsp, allj, alla, allm]

		scoreTrack = [1] * len(sentence)

		for j in range(1, len(allindex)):
			for k in allindex[j]:
				scoreTrack[k] = sum([scoreTrack[p] for p in allindex[j-1] if p < k])

		total = 0
		for x in allm:
			total += scoreTrack[x]
		totalStr = str(total)[-4:]
		if len(totalStr) != 4:
			for m in range(len(totalStr), 4):
				totalStr = '0' + totalStr
		print('Case #%d: ' % (i + 1) + totalStr)

def find(s, ch):
	return [i for i, ltr in enumerate(s) if ltr == ch]

main()