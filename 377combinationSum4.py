import time
class Solution:
    def combinationSum4(self, nums, target):
        res = []
        self.dfs(nums, target, [], res)
        return len(res)

    def dfs(self, nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for num in nums:
            self.dfs(nums, target-num, path+[num], res)

    def combinationSum41(self, nums, target):
        nums = sorted(nums)
        comb = [1] + [0]*target
        for i in range(1, len(comb)):
            for num in nums:
                if num > i: break
                # if num == i: comb[i] += 1
                # if num < i: comb[i] += comb[i - num]
                comb[i] += comb[i - num]
        return comb[target]


obj = Solution()
print (obj.combinationSum4([1,2,3], 4))

