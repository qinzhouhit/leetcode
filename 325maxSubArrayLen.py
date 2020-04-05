'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        dict_ = {}
        sum_ = 0; maxLen = 0

        for i in range(len(nums)):
            sum_ += nums[i]

            if sum_ == k:
                maxLen = i + 1

            elif sum_ - k in dict_:
                maxLen = max(maxLen, i - dict_[sum_ - k])

            if sum_ not in dict_:
                dict_[sum_] = i

        return maxLen

obj = Solution()
print (obj.maxSubArrayLen([1, -1, 5, -2, 3], 3))
