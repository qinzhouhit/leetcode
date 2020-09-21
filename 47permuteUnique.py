'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


from collections import Counter

class Solution:
    
    '''
    The worst-case time complexity is O(n! * n).
    For any recursive function, the time complexity is 
    O(branches^depth) * amount of work at each node in the recursive call tree. 
    However, in this case, we have n*(n-1)*(n*2)*(n-3)*...*1 branches at each 
    level = n!, so the total recursive calls is O(n!)
    We do n-amount of work in each node of the recursive call tree, (a) the 
    for-loop and (b) at each leaf when we add n elements to an ArrayList. 
    So this is a total of O(n) additional work per node.
    '''
    def permuteUnique4(self, nums):
        res = []
        if not nums: return res
        used = [False] * len(nums)
        path = []
        nums.sort()
        self.dfs3(nums, used, path, res)
        return res
    
    def dfs3(self, nums, used, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]: 
                continue
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue # 
            used[i] = True
            path.append(nums[i])
            self.dfs(nums, used, path, res)
            used[i] = False
            path.pop()
    
    
    ######
    # backtrack version
    def permuteUnique3(self, nums):
        self.res=[]
        def dfs(tmp, counter):
            if len(tmp)==len(nums):
                self.res.append(tmp[:])
            for x in counter: # skip duplicates
                if counter[x]>0:
                    tmp.append(x)
                    counter[x]-=1
                    dfs(tmp, counter)
                    tmp.pop()
                    counter[x]+=1
        dfs([],Counter(nums))
        return self.res
    
    
    #####
    # self-made
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if len(path) == len(nums) and path not in res:
                res.append(path[:])
            
            for num in ct:
                # print ("what")
                if ct[num] > 0:
                    ct[num] -= 1
                    path.append(num)
                    backtrack(nums, path)
                    path.pop()
                    ct[num] += 1
        
        res = []
        ct = Counter(nums)
        # print (ct)
        backtrack(nums, [])
        return res
    
    
    ######
    # a version based on 46
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums and path not in res:
            res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

obj=Solution()
print(obj.permuteUnique([1,1,3]))
