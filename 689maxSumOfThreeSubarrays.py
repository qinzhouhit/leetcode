'''
keys: Why using three consecutive intervals? Why are the swapping mechnism?
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # O(N) for S and T
    # https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108231/C%2B%2BJava-DP-with-explanation-O(n)
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        w = [] # for all the sum of subarrays, from left to right
        cur_sum = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            if idx >= k:
                cur_sum -= nums[idx-k] # left most element in the window
            if idx >= k - 1:
                w.append(cur_sum)
                
        # fix the middle subarray, find the index of left/ right subarray with max sum
        left = [0] * len(w) # till the current idx, the beginning index of the subarray with max sum
        max_idx = 0
        for i in range(len(w)):
            if w[i] > w[max_idx]: # if equal, we don't swap, since we want the smaller index
                max_idx = i
            left[i] = max_idx

        right = [0] * len(w)
        max_idx = len(w) - 1
        for i in range(len(w)-1, -1, -1):
            if w[i] >= w[max_idx]: # when equal, swap, since we want the smaller index (from right to left)
                max_idx = i
            right[i] = max_idx

        ans = None
        for j in range(k, len(w) - k): # j is the beginning index of middle subarray
            i, l = left[j-k], right[j+k]
            if ans is None or (w[i]+w[j]+w[l] > w[ans[0]]+w[ans[1]]+w[ans[2]]):
                ans = i, j, l
        return ans
            
    
    
    
    
    
    