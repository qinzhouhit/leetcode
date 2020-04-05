'''
keys:
Solutions:
Similar:
T:
S:
'''

# import copy
# class Solution:
#     def combine(self, n, k):
#         res=[]; tmp=[]
#         self.helper(res, tmp, 1, n, k)
#         return res
#
#     def helper(self, res, tmp, start, n, k):
#         if len(tmp)==k:
#             res.append(tmp[:])
#             return
#
#         for i in range(start, n+1):
#             tmp.append(i)
#             self.helper(res, tmp, i+1, n, k)
#             tmp.pop()

class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) \
                for pre in self.combine(i-1, k-1)]

obj=Solution()
print(obj.combine(4,2))
