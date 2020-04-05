'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def getFactors(self, n):
        res = []
        self.dfs(n, 2, [], res)
        return res

    def dfs(self, n, start, path, res):
        while start*start <= n:
            if n % start == 0:
                res.append(path + [start, n//start])
                self.dfs(n//start, start, path + [start], res)
            start += 1
        return res

obj = Solution()
print (obj.getFactors(10))
