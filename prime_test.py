'''Test execution time between two different prime number algorithms.'''

import timeit

def find_primes(n):
    primeList = []
    for x in range(2, n):
        isPrime = True
        for y in range(2, int(x**0.5)+1):
            if x % y  == 0:
                isPrime = False
                break

        if isPrime:
            primeList.append(x)

    return(primeList)


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

x = 11
assert(len(sieve_primes(x)) == len(find_primes(x)))
assert(sieve_primes(x) == find_primes(x))
print("Tests pass")


x = 1000001
starttime = timeit.default_timer()
sieve_primes(x)
print("Time to sieve primes: ", timeit.default_timer() - starttime)
starttime = timeit.default_timer()
find_primes(x)
print("Time to find primes: ", timeit.default_timer() - starttime)


#print(sieve_primes(11))
#print(find_primes(11))
