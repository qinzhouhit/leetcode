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



    # self-made
    # T: O(k * C_N^k), C_N^k: number of combinations selectiong k out of N
    # the time consuming part is to append the built combination of length k to the output
    # S: O(C_N^k) for the combination output
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        
        def dfs(idx, path, ct):
            if ct == 0:
                res.append(path[:])
                return

            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i+1, path, ct-1) # starting from i+1
                path.pop()
            
        res = []
        dfs(0, [], k)
        return res


obj=Solution()
print(obj.combine(4,2))
