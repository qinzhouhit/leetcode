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
