'''
keys: stack
Solutions:
Similar: 
T:
S:
'''
from typing import List

'''
monotonous increase stack
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
Application: find previous less element of each element in a vector with O(n) time

### previous_less[i] = j means A[j] is the previous less element of A[i].
### previous_less[i] = -1 means there is no previous less element of A[i].
def previous_less(A):
	n = len(A)
	pre_less = [-1] * n
	stack = []
	for i in range(n):
		while stack and A[i] < A[stack[-1]]:
			stack.pop()
		pre_less[i] = -1 if not stack else stack.pop()
		stack.append(i)


### next_less[i] = j means A[j] is the next less element of A[i].
### next_less[i] = -1 means there is no next less element of A[i].
def next_less(A):
	n = len(A)
	nxt_less = [-1] * n
	stack = []
	for i in range(n):
		while stack and A[i] < A[stack[-1]]:
			x = stack[-1]
			stack.pop()
			nxt_less[x] = i
		stack.append(i)
'''

# based on the above concept: 
# the distance means the number of vals larger than A[i] on the left/right
# Denote by left[i] the distance between element A[i] and its PLE.
# Denote by right[i] the distance between element A[i] and its NLE.
# The final answer is,
# sum(A[i]*left[i]*right[i] )
class Solution:
	def sumSubarrayMins(self, arr: List[int]) -> int:
		A = arr
		n = len(A)
		stack_left = []; stack_right = []
		left = [0] * n; right = [0] * n
		# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step/194366
		for i in range(n): # initialize, assuming the dummy val at idx -1?
			left[i] = i + 1
		for i in range(n):
			right[i] = n - i

		for i, val in enumerate(A):

			# for previous less
			while stack_left and val < stack_left[-1][0]:
				stack_left.pop()
			left[i] = i+1 if not stack_left else i - stack_left[-1][1]
			stack_left.append((val, i))

			# for next less
			while stack_right and val < stack_right[-1][0]:
				x = stack_right[-1]
				stack_right.pop()
				right[x[1]] = i - x[1]
			stack_right.append((val, i))

		res = 0
		mod = 1e9 + 7
		for i, val in enumerate(A):
			res = (res + val * left[i] * right[i]) % mod
		return int(res)


	### a version without weird initialization
	def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right = [0] * n, [0] * n 
        left_stack, right_stack = [], []
        for i in range(n):
            count = 1
            while left_stack and left_stack[-1][0] > A[i]: 
            	count += left_stack.pop()[1]
            left[i] = count
            left_stack.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while right_stack and right_stack[-1][0] >= A[i]: 
            	count += right_stack.pop()[1]
            right[i] = count
            right_stack.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod



class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
    	m = 10**9 + 7

    	stack = []
    	res = dot = 0
    	for i, val in enumerate(arr):
    		# adding all res for subarray [i, j], i <= j
    		ct = 1
    		while stack and y <= stack[-1][0]:
    			x, c = stack.pop()
    			ct += c
    			dot -= x * c

    		stack.append((y, count))
    		dot += y * count
    		res += dot
    	return res % m
