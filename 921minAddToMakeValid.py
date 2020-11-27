'''keys: Solutions:Similar:T:S:'''from typing import Listclass Solution:        # stack; O(N) for S and T    def minAddToMakeValid1(self, S: str) -> int:        stack = []        for s in S:            if s == ")" and stack and stack[-1] == "(":                stack.pop()            else:                stack.append(s)        return len(stack)                   # T: O(N), S: O(1)    '''    Keep track of the balance of the string: the number of '(''s minus the     number of ')''s. A string is valid if its balance is 0, plus every prefix     has non-negative balance.    '''    def minAddToMakeValid(self, S: str) -> int:        ans = bal = 0        for symbol in S:            bal += 1 if symbol == '(' else -1            # It is guaranteed bal >= -1            if bal == -1:                ans += 1                bal += 1        return ans + bal