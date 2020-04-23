'''
keys:
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
    def trap(self, height):
        res = 0
        n = len(height)
        for i in range(n):
            l = max(height[0: i+1]) # from leftmost to current element
            r = max(height[i: n]) # from current to rightmost element
            res += (min(l, r) - height[i])
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

    # two pointer, T: O(n), S: O(1)
    def trap3(self, height):
        n = len(height)
        if n == 0: return 0
        l, r = 0, n-1
        max_l = height[l]; max_r = height[r]
        res = 0
        while l < r:
            if max_l < max_r:
                res += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return res



obj = Solution()
print (obj.trap3([0,1,0,2,1,0,1,3,2,1,2,1]))
