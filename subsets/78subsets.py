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

    # educative.io, bfs
    # T: the number of subsets doubles as we add each element to all the existing subsets,
    # therefore, we will have a total of O(2^N) subsets
    # we construct a new subset from an existing set, therefore, the time complexity of 
    # the above algorithm will be O(N*2^N).
    # S: O(N*2^N), i.e., O(2^N) subsets and each one takes O(N)
    def subsets4(self, nums):
        subsets = []
        subsets.append([])
        for num in nums:
            n = len(subsets)
            for i in range(n):
                tmp = list(subsets[i])
                tmp.append(num)
                subsets.append(tmp)
        return subsets


    # DFS recursively, T and S: O(N*2^N)
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

        def helper(path, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                self.helper(path, i+1)
                path.pop()

        res = []
        helper([], 0)
        return res

    
    # TODO: huahua
    def subsets3(self, nums):
        res = []
        for i in range(len(nums)+1):
            self.dfs3(i, 0, [], res, nums)
        return res

    def dfs3(self, n, start, cur, res, nums):
        if n == len(cur):
            res.append(cur.copy())
            return
        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.dfs3(n, i+1, cur, res, nums)
            cur.pop()

    # self-made
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, path):
                # if idx == len(path):
                res.append(path[:])
                for i in range(idx, len(nums)):
                    helper(i+1, path + [nums[i]])
                
        res = []
        helper(0, [])
        return res



obj=Solution()
print(obj.subsets1([1,2,3]))
