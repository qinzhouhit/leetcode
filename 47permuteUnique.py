from collections import Counter

class Solution:
    def permuteUnique(self, nums):
        self.res=[]
        def dfs(tmp, counter):
            if len(tmp)==len(nums):
                self.res.append(tmp[:])
            for x in counter:
                if counter[x]>0:
                    tmp.append(x)
                    counter[x]-=1
                    dfs(tmp, counter)
                    tmp.pop()
                    counter[x]+=1
        dfs([],Counter(nums))
        return self.res

obj=Solution()
print(obj.permuteUnique([1,1,3]))
