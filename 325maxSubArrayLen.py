'''
keys: use dict to keep track of; prefix sum
Solutions:
Similar:
T: O(n)
S: O(n)
'''
from typing import List

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    
    def maxSubArrayLen1(self, nums: List[int], k: int) -> int:
        res, acc = 0, 0
        # This way, whenever acc = 0 in your subarray, the value at
        # mp[0] remains -1 instead of being changed to the current 
        # index, i. You want to include consecutive values in your 
        # subarray that total to 0 in order to get the longest 
        # subarray count that sums up to k.
        h = {0:-1} 
        
        for idx, val in enumerate(nums):
            acc += val
            if acc not in h:
                h[acc] = idx
            if acc - k in h:
                res = max(res, idx - h[acc-k])
        # print (h)
        return res
    
    # O(n) for S and T
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Write your code here
        dict_ = {}
        sum_ = 0; maxLen = 0

        for i in range(len(nums)):
            sum_ += nums[i]

            if sum_ == k:
                maxLen = i + 1

            elif sum_ - k in dict_: # cur: sum_; pre: sum_ - k; subtract: k
                maxLen = max(maxLen, i - dict_[sum_ - k])

            if sum_ not in dict_:
                dict_[sum_] = i

        return maxLen

obj = Solution()
print (obj.maxSubArrayLen([1, -1, 5, -2, 3], 3))
