'''
keys:
if n is not prime <=> n=a*b, a<=b => a <= sqrt(n)
Solutions:
Similar:
T: n*sqrt(n) (if you just search until sqrt(n)
S: O(1)
'''

class Solution:
    # T(n): nloglogn, close to linear
    # S: O(n)
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # prime*someNumber is not prime
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)



