'''
keys: stack
Solutions:
Similar: 
T:
S:
'''
from typing import List

'''
the numbered jump meaning the order of the jumps
1st jump means the first jump, etc. You can only jump forward.

'''

class Solution:


	# official
	def oddEvenJumps(self, arr: List[int]) -> int:
    	A = arr
		N = len(A)

        def make(B): # generate the results for next jumps
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key = lambda i: A[i])
        # the index where i jumps to if this is an odd numbered jump
        # because we jump to min(larger numbers)
        oddnext = make(B) 
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        # initialize odd and even lists that will contain
        # the information of if the end can be reached
		# from the respective index
        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True # since we reached the end

        for i in range(N-2, -1, -1):
        	# if an odd jump is available from current index,
            # check if an even jump landed on the index of the available
            # odd jump and set current index in odd to True if it did
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum(odd)

	# T: O(NlogN), S: O(N), N as length of arr
	# https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
    def oddEvenJumps(self, arr: List[int]) -> int:
    	A = arr
    	n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)





    	

        