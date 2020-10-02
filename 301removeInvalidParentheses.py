'''keys: https://www.youtube.com/watch?v=2k_rS_u6EBkSolutions: no dp solution for this oneSimilar: T:S:'''from typing import Listclass Solution:    # T: O(n^(l+r))    # S: O((l+r)^2)    def isValid(self, s):        ct = 0        for c in s:            if c == "(": ct +=1             if c == ")": ct -= 1            if ct < 0: return False        return ct == 0        def dfs(self, s, start, l, r):        if l == 0 and r == 0:            if self.isValid(s):                self.ans.append(s)                return                for i in range(start, len(s)):            if i != start and s[i] == s[i-1]:                continue # We only remove the first parenthes if there are consecutive ones to avoid duplications.                        if s[i] == "(" or s[i] == ")":                curr = s                curr = curr[:i] + curr[i+1:] # remove c at index i                if r > 0 and s[i] == ")":                    self.dfs(curr, i, l, r-1)                elif l > 0 and s[i] == "(":                    self.dfs(curr, i, l-1, r)                        def removeInvalidParentheses(self, s: str) -> List[str]:        l, r = 0, 0        for c in s:            l += (c == "(") # ct of left parentheses            if l == 0: # no remaining left parentheses                r += (c == ")") # ct of single right parenthese            else: # with remaining left parentheses                l -= (c == ")") # cancelling pairs                self.ans = []        self.dfs(s, 0, l, r)        return self.ans            sol = Solution()print (sol.removeInvalidParentheses("()())()"))                                            