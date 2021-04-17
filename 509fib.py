'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# T: O(2^n), S: O(n)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


    # Bottom-Up Approach using Memoization
    # O(n) for S and T
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]


    # Top-Down Approach using Memoization
    # O(N) for S and T
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)


    # Iterative Top-Down Approach
    # O(N) for T and O(1) for S
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current



    # math O(1) for S and T
    def fib(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)












