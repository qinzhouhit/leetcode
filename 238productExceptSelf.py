'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:

    # T: O(N), S: O(1) if output space doesn't count
    def productExceptSelf(self, nums):
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * p
            p *= nums[i]
        return res

o = Solution()
o.productExceptSelf([1,2,3,4])
