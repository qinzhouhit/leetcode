'''
keys: two pointers, get the max of left subset and right subset and 
use the min of the two max as water level. Use the 
Solutions:
Similar:
T:
S:
'''

# https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.

class Solution:
    # method 1: brute force
    # T: O(n^2), S:(1)
    import heapq
    def trap3(self, height):
        res = 0
        n = len(height)
        for i in range(n): # the idx in below ranges are important
            l = max(height[0: i+1]) # from leftmost to current element, inclusive
            r = max(height[i: n]) # from current to rightmost element, including i
            res += (min(l, r) - height[i])
        return res

    # dp based on above method
    def trap4(self, height):
        if not height:
            return 0
        res = 0
        n = len(height)
        left_max = [0]*n; right_max = [0]*n
        left_max[0] = height[0]
        for i in range(1, n): # left_max[i] means from 0 to i, inclusive
            left_max[i] = max(height[i], left_max[i-1])
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, n-1):
            res += min(left_max[i], right_max[i]) - height[i]
        return res


    # two pointer, T: O(n), S: O(1)
    # https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
    # instead of calculating area by height*width, sum water amount of each bin(width=1).
    # maintain a max height of left and right separately, which is like a one-side wall of partial container.
    # Fix the higher one and flow water from the lower part. For example, if current height of 
    # left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.
    def trap2(self, height):
        n = len(height)
        if n == 0: return 0
        l, r = 0, n-1
        max_l = height[l]; max_r = height[r]
        res = 0
        while l < r:
            # the equal case being in any loop is fine
            if max_l < max_r: # left is low
                res += max_l - height[l] # fill water for cur bin, i.e., idx = l
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return res


    # DP, T: O(n), S: O(n)
    def trap1(self, height):
        n = len(height)
        l = [0]*n; r = [0]*n
        res = 0
        # l[i]: max of height[0:i+1]; r[i]: max of height[i:n]
        # l[i] = max(height[i], l[i-1]), i: 0 ~ n-1
        # r[i] = max(height[i], r[i]), i: n-1 ~ 0
        for i in range(n): # i==0 is the corner case for l[i-1]
            # if no i == 0, then l[-1] => out of range
            l[i] = height[i] if i == 0 else max(height[i], l[i-1])
        for i in range(n-1, -1, -1):
            r[i] = height[i] if i == n-1 else max(height[i], r[i+1])
        for i in range(n):
            res += (min(l[i], r[i]) - height[i])
        return res



obj = Solution()
print (obj.trap3([0,1,0,2,1,0,1,3,2,1,2,1]))
