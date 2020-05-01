def sieve_primes(n):
	sieve = [i for i in range(2,n)]
	primes = []
	p = 0

	while p < len(sieve):
		for i in range(p+sieve[p],len(sieve),sieve[p]):
			sieve[i] = 0
		p+=1
		while p < len(sieve) and sieve[p] == 0:
			p+=1
		

	for i in range(0, len(sieve)):
		if sieve[i] != 0:
			primes.append(sieve[i])
	return primes

print(sieve_primes(1001))
