'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # def permute(self, nums):
    #     res = []
    #     self.dfs(nums, [], res)
    #     return res
    #
    # def dfs(self, nums, path, res):
    #     if not nums:
    #         res.append(path)
    #         # return # backtracking
    #     for i in range(len(nums)):
    #         # nums[:i]+nums[i+1:] will be nums excluding i
    #         self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    def permute(self, nums):
        self.res=[]
        def dfs(nums, tmp):
            if len(tmp)==len(nums):
                print (tmp)
                self.res.append(tmp[:])

            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                dfs(nums, tmp)
                tmp.pop()
        dfs(nums,[])
        return self.res

obj=Solution()
print(obj.permute([1,2,3]))
