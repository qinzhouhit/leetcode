'''
keys:
Solutions:
Similar:
T:
S:
'''

import math

class Solution:
    def getPermutation(self, n, k):
        nums=list(range(1, n+1))
        per=""
        k-=1
        while n>0:
            n-=1
            ind, k=divmod(k, math.factorial(n))
            # NN = reduce(operator.mul, elements) # n!
            per+=str(nums[ind])
            nums.remove(nums[ind])
        return per


obj=Solution()
print (obj.getPermutation(4,5))
