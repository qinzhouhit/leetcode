class Solution:
    def grayCode(self, n):
        res=[0]
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j] | 1<<i)
        return res

obj=Solution()
print (obj.grayCode(2))
