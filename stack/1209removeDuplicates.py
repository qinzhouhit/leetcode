'''
keys:
Solutions:
Similar: 1047
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893/JavaC++Python-Two-Pointers-and-Stack
	# stack with revision
	# O(N) for S and T
    def removeDuplicates(self, s: str, k: int) -> str:
    	stack = [["#", 0]] # cant use tuple here since unable to index
        for c in s:
            if stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop() # notice that you actually pop k chars at one time
        return "".join(k*c for c, k in stack)


    # two pointers
    def removeDuplicates1(self, s: str, k: int) -> str:
    	i = 0; n = len(s)
        ct = [0] * n
        res = list(s)
        for j in range(n):
            res[i] = res[j] # assign val for i-idx in res
            if i > 0 and res[i-1] == res[i]: # if duplicated
                ct[i] = ct[i-1] + 1 # increase the ct
            else:
                ct[i] = 1
            if ct[i] == k:
                i -= k # back i-idx by k, s.t. i will be on the right position after i += 1
            i += 1
        return "".join(res[:i])