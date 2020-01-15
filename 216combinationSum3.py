class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0: return
        if k ==0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            print ("k-1: {}, nums[i]: {}, n-nums[i]: {}, index+1: {}, path: {}, res: {}".\
                   format(k-1, nums[i], n-nums[i], index+1, path, res))
            self.dfs(nums, k-1, n-nums[i], index+1, path+[nums[i]], res)
            # change the i+1 to index+1, then the res will contain duplicate ints

obj = Solution()
print (obj.combinationSum3(3, 9))
