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
    # O(N) for S and T
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()
        # q: monotonous decreasing
        # make sure the rightmost one is the smallest/ leftmost one is the biggest
        for idx, num in enumerate(nums):
            while q and num >= nums[q[-1]]:
                q.pop()
            # add current num idx anyway
            q.append(idx)
            # make sure the leftmost one is in-bound
            # check this first, corner case: [1, -1], 1
            if idx - q[0] >= k:
                q.popleft()
            # once having k elements, we append the cur max to the res
            if idx >= k - 1: # e.g., having at least k elements now
                res.append(nums[q[0]])
        return res



    # T: O(N*k); S: O(N-k+1) for output
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        
        return [max(nums[i:i + k]) for i in range(n - k + 1)]





obj = Solution()
print (obj.maxSlidingWindow([5,3,4,1,6,2,2,4,3,1,5], 3))
