'''keys: https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C%2B%2B-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanationSolutions:Similar: T:S:'''from typing import Listimport collectionsclass Solution:    # dp    ''' P as positive subset, N as negative subset    sum(P) - sum(N) = target    sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)    2 * sum(P) = target + sum(nums) # so target + sum(nums) can't be odd    '''    def findTargetSumWays3(self, nums: List[int], S: int) -> int:        sum_ = sum(nums)        # if (S + sum_) & 1 means odd        if ((S + sum_) & 1) or sum_ < S:            return 0        else:            return self.helper1(nums, (S + sum_)//2)            def helper1(self, nums, S):        dp = [0] * (S+1) # dp[i] means ways to reach the sum i        dp[0] = 1        for i in range(len(nums)):            for j in range(S, nums[i]-1, -1):                dp[j] += dp[j - nums[i]]        return dp[S]                def findTargetSumWays(self, nums, S):        count = collections.defaultdict(int)        count[0] = 1 # k: sum, v: ways of reach k (the sum)        for x in nums:            step = collections.defaultdict(int)            for y in count:                step[y + x] += count[y]                step[y - x] += count[y]            count = step            return count[S]    # lru_cache    def findTargetSumWays2(self, nums: List[int], S: int) -> int:                @lru_cache(maxsize=None)        def helper(i, s): # i as idx            ct = 0 # number of ways            if i == len(nums):                if s == 0:                     ct = 1            else:                ct = helper(i+1, s-nums[i]) + helper(i+1, s+nums[i])            return ct                return helper(0, S) # or you can start at 0, summing up to S        # recursion + memo    # T and S: O(l*n)    def findTargetSumWays1(self, nums: List[int], S: int) -> int:                def helper(i, s):            if (i, s) not in memo:                r = 0                if i == len(nums):                    if s == 0:                        r = 1                else:                    r = helper(i+1, s-nums[i]) + helper(i+1, s+nums[i])                memo[(i, s)] = r            return memo[(i, s)]                memo = {}        return helper(0, S)            # recursion, TLE    # T: O(2^n); S: O(n), n = len(nums)    def findTargetSumWays(self, nums: List[int], S: int) -> int:        self.ct = 0        self.helper(nums, 0, 0, S)        return self.ct        def helper(self, nums, i, sum_, S):        if i == len(nums):            if sum_ == S:                self.ct += 1        else:            self.helper(nums, i+1, sum_+nums[i], S)            self.helper(nums, i+1, sum_-nums[i], S)        