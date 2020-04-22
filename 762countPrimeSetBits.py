'''
keys:
bin(5) = '0b101'
at most 1,000,000, so the numbers can be at most 20 bits.
Solutions:
Similar:
T: n*sqrt(n) (if you just search until sqrt(n)
S: O(1)
'''


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2,3,5,7,11,13,17,19]
        res = 0
        for i in range(L, R+1):
            if bin(i).count('1') in primes:
                res += 1
        return res
