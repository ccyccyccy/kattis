primes = [2,3,5,7,11,13]
factors = []

def main():
	while True:
		num = int(input())
		if num == 4:
			return
		fillPrimesTo(num)
		print(primes)
		if isPrime(num):
			print(num)
			continue
			'''
		primeReduce(num)
		summ = sum(factors)
		while not isPrime(summ):
			factors.clear()
			primeReduce(summ)
			summ = sum(factors)
		print(sum)
		factors.clear()'''

		

def isPrime(n):
	if n > primes[-1]:
		fillPrimesTo(n+3)
	return n in primes

def fillPrimesTo(n):
	for i in range(primes[-1], n + 3, 2):
		primes.append(i)
		for prime in primes[:-1]:
			if i % prime == 0:
				print(prime)
				primes.pop()

def primeReduce(n):
	if isPrime(n):
		return n

	for prime in primes:
		if n % prime == 0:
			factors.append(prime)
			primeReduce(n / prime)
			break

main()