'''
keys: two pointers
Solutions:
Similar:
T:
S:
'''

class Solution:
	# O(n) for T and O(1) for S
	def maxArea1(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1 # inclusive idx
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea


    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

obj=Solution()
print (obj.maxArea([1,8,6,2,5,4,8,3,7]))
