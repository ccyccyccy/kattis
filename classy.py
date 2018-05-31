def main():
	cases = int(input())
	for case in range(cases):
		npeople = int(input())
		peoples = []
		for people in range(npeople):
			inp = input()
			name = inp.split(' ')[0][:-1]
			clas = inp.split(' ')[1].split('-')
			peoples.append(Person(name, clas))
		peoples.sort(reverse=True)
		for people in peoples:
			print(people.name)
		print('==============================')

class Person:
	def __init__(self, name, clas):
		self.name = name
		self.clas = clas

	def __lt__(self, other):
		selfLength = len(self.clas)
		otherLength = len(other.clas)
		for i in range(1, max(selfLength, otherLength) + 1):
			selfCurrent = self.indexClass(i)
			otherCurrent = other.indexClass(i)
			if selfCurrent != otherCurrent:
				return selfCurrent < otherCurrent
		return self.name > other.name

	def indexClass(self, indexFromBack):
		if indexFromBack > len(self.clas):
			return 'middle'
		return self.clas[-indexFromBack]

main()