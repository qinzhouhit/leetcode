'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

obj=Solution()
print (obj.removeElement([0,0,1,1,1,2,2,3,3,4], 1))
