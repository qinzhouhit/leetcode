'''
keys: DFS + backtracking
Solutions:
Similar:
T: O(n*2^n)
S: O(n)
'''

class Solution:

    # iterative, O(n * 2^n)
    # def subsets(self, nums):
    #     res = [[]]
    #     for num in nums:
    #         res += [r + [num] for r in res]
    #     return res

    # def subsets(self, nums):
    #     all_subsets = [[]]
    #     if not nums:
    #         return all_subsets
    #     for num in nums:
    #         for idx in range(len(all_subsets)):
    #             all_subsets.append(all_subsets[idx]+[num])
    #     return all_subsets

    # DFS recursively
    def subsets1(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


    # TODO: DFS backtracking
    def subsets(self, nums):
        res=[]; path=[]
        self.helper(res, path, 0, nums)
        return res

    def helper(self, res, path, start, nums):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.helper(res, path, i+1, nums)
            path.pop()


    # TODO: huahua
    def subsets3(self, nums):
        res = []
        for i in range(len(nums)+1):
            self.dfs(i, 0, [], res, nums)
        return res

    def dfs(self, n, start, cur, res, nums):
        if n == len(cur):
            res.append(cur.copy())
            return
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.dfs(n, i+1, cur, res, nums)
            cur.pop()




obj=Solution()
print(obj.subsets1([1,2,3]))
