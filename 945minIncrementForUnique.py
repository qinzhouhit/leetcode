'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:

    # https://leetcode.com/problems/minimum-increment-to-make-array-unique/discuss/197687/JavaC%2B%2BPython-Straight-Forward
    # T: O(NlogN)
    # Sort the input array.
    # Compared with previous number,
    # the current number need to be at least prev + 1.
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0; prev = A[0]
        for i in range(1, len(A)):
            expect = prev + 1
            res += 0 if A[i] > expect else expect - A[i]
            prev = max(expect, A[i])
        return res



    # official
	# O(N) for S and T, N as the max length
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        taken = [] # values for later consideration

        ans = 0
        for x in range(100000):
            if count[x] >= 2: # take the duplicated values away for now
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop() # we increase the taken values to x
        return ans
