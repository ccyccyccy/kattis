def main():
	testcases = int(input())
	for j in range(1, testcases + 1):
		print('Case #%d:' % j)
		nsongs = int(float(input()))
		if nsongs == 1:
			input()
			print('""')
			continue
		songs = []
		for i in range(nsongs):
			songs.append(input().upper())

		for song in songs:
			potentialstrings = []
			othersongs = songs[:]
			othersongs.remove(song)
			for i in range(1, len(song) + 1): # For each length of substring to test, from 1 to full name
				for j in range(len(song) - i + 1): # For each start of substring of song to search
					substring = song[j : j + i]
					fail = False
					for othersong in othersongs:
						if substring in othersong:
							fail = True
							break
					if fail == False:
						potentialstrings.append(substring)
				if len(potentialstrings) != 0:
					break
			if len(potentialstrings) == 0:
				print(':(')
			else:
				print('"' + min(potentialstrings) + '"')



main()