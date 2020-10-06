'''keys:Solutions:Similar:T:S:'''from typing import Listclass Solution:        # O(n) for S and T    def findMaxLength(self, nums: List[int]) -> int:        hashmap = {}        maxLen = 0; ct = 0        for i in range(len(nums)):            if nums[i] == 1:                ct += 1            else:                ct -= 1            if ct == 0:                maxLen = max(maxLen, i+1)            # meaning we have seen equal number of 0s and 1s between             # hashmap[ct] and i            if ct in hashmap:                 maxLen = max(maxLen, i - hashmap[ct])            else:                hashmap[ct] = i        return maxLen                            # O(N) for S and T    def findMaxLength1(self, nums: List[int]) -> int:        n = len(nums)        arr = [-2] * (2 * n + 1)        arr[n] = -1        maxLen = 0; ct = 0        for i in range(n):            if nums[i] == 0:                ct -= 1            else:                ct += 1            if arr[ct + n] >= -1:                maxLen = max(maxLen, i - arr[ct + n])            else:                arr[ct + n] = i        return maxLen                                                    