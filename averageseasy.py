numberOfTestcases = int(input())

for j in range(numberOfTestcases):
	input()
	ncs, ne = input().split(' ')
	ncs = int(ncs)
	ne = int(ne)
	csiq = [int(iq) for iq in input().split(' ')]
	eiq = [int(iq) for iq in input().split(' ')]
	tcsiq = sum(csiq)
	teiq = sum(eiq)
	oacsiq = tcsiq/ncs
	oaeiq = teiq/ne
	ntransfergood = 0
	for transfer in csiq:
		acsiq = (tcsiq - transfer)/(ncs-1)
		aeiq = (teiq + transfer)/(ne+1)
		if acsiq > oacsiq and aeiq > oaeiq:
			ntransfergood += 1
	print(ntransfergood)