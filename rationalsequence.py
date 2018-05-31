from fractions import Fraction

ndata = int(input())
for data in range(ndata):
	fn = Fraction(input().split(' ')[1])
	numerator = fn.numerator
	denominator = fn.denominator
	if numerator < denominator:
		ansNumerator = denominator
		ansDenominator = ansNumerator - numerator
	elif numerator > denominator:
		ansNumerator = denominator
		layers = int(numerator / denominator)
		numerator = numerator % denominator
		topDenominator = denominator - numerator
		rightNumerator = topDenominator + numerator
		ansDenominator = topDenominator + rightNumerator * layers
	else:
		ansNumerator = 1
		ansDenominator = 2
	print('%d %d/%d' % (data+1, ansNumerator, ansDenominator))