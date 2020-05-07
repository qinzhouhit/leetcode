'''
keys: backtracking
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # T: O(n*2^n), n for isPar, 2^n for ways to split the string into substring
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path[:]) # deep copy
            return
        for i in range(1, len(s)+1):
            if self.isPar(s[:i]):
                path.append(s[:i])
                self.dfs(s[i:], path, res)
                path.pop()

    def isPar(self, s):
        return s == s[::-1]


sol = Solution()
print (sol.partition("aab"))
