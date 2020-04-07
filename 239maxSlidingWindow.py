'''
keys: deque store index, but not all the index, only the ones in the window
Solutions:
Similar:
T: O(n)
S: O(k)
'''
#
# # TODO: brutal force
# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         if not nums or k <= 0:
#             return
#         if len(nums) == k:
#             return max(nums)
#         else:
#             res = []
#             for i in range(len(nums)-k+1):
#                 max_ = 0
#                 for j in range(i,i+k):
#                     max_ = max(max_, nums[j])
#                 res.append(max_)
#             return res

# TODO: deque
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        dq = deque()
        # make sure the rightmost one is the smallest/ leftmost one is the biggest
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] <= n:
                dq.pop()
            # add in
            dq += [i]
            # make sure the leftmost one is in-bound
            if i - dq[0] >= k:
                dq.popleft()
            # if i + 1 < k, then we are initializing the dq array
            if i + 1 >= k:
                res.append(nums[dq[0]])
        return res



obj = Solution()
print (obj.maxSlidingWindow([5,3,4,1,6,2,2,4,3,1,5], 3))
