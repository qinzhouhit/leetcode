'''keys: Solutions:Similar:T:S:'''from typing import Listclass Solution:    # a tricky one; T: O(N); S: O(N)     def maxProduct(self, nums: List[int]) -> int:        rev = nums[::-1]        for i in range(1, len(nums)):            # prefix product            # if nums[i-1] != 0: nums[i] *= nums[i-1]            nums[i] *= nums[i-1] or 1            # suffix product            rev[i] *= rev[i-1] or 1        return max(nums + rev)                