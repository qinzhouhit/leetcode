'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def productExceptSelf(self, nums):
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            print (res)
            p *= nums[i]
        print ('second pass')
        p = 1
        for i in range(len(nums)-1, -1, -1):
            print (res)
            res[i] = res[i] * p
            p *= nums[i]
        print (res)
        return res

o = Solution()
o.productExceptSelf([1,2,3,4])
