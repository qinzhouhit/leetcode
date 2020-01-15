class Solution:
    def permute(self, nums):
        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], res)

obj = Solution()
print (obj.permute([1,2,3]))
