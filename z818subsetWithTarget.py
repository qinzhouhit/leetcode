'''keys: two pointersSolutions:Similar:T:S:'''from typing import List# https://code.dennyzhang.com/subset-with-targetclass Solution:    # T: O(n*log(n)), S: O(n)    def subsetWithTarget(self, nums, target):        nums.sort()        res = 0        left, right = 0, len(nums)-1        while left <= right:            v = nums[left] + nums[right]            if v >= target:                right -= 1                continue            # now v < target. whether we can choose the left            res += pow(2, (right-left)) # number of subsets in a set            left += 1        return res