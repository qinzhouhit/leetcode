'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # brute force, T: O(n^2), S: O(n)
    def productExceptSelf(self, nums):
        products = [0] * len(nums)

        for i in range(len(nums)):
            curProduct = 1
            for j in range(len(nums)):
                if i != j:
                    curProduct *= nums[j]
            products[i] = curProduct
        return products


    '''
    Suppose you have numbers:
    Numbers [1 2 3 4 5]
    Pass 1: [- 1 12 123 1234], for p
    Pass 2: [2345 345 45 5 -], for p
    Finally, you multiply ith element of both the lists to get:
    Pass 3: [2345, 1345, 1245, 1235, 1234]
    '''

    # T: O(N), S: O(1) if output space doesn't count
    def productExceptSelf(self, nums):
        p = 1
        res = []
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

o = Solution()
o.productExceptSelf([1,2,3,4])
