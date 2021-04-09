'''
keys: two pointers
Solutions:
Similar:
T: O(n^2)
S: O(1) for res
'''



class Solution:
    ##### O(nLogn + nn) => O(n^2)
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # We do not need to consider i after nums[i]>0, (already sorted!)
            # since sum of 3 positive will be always greater than zero.
            if nums[i] > 0: break
            # If the number is the same as the number before,
            # we have used it as target already
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # exclude possible duplicate triplets
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1 # search for new combinations
        return res


    ##### educative.io version, two pointers
    # T: O(n^2), S: O(logn) to O(n), depending on sort
    def threeSum1(self, nums):
        nums.sort()
        triplets = []
        
        def helper(nums, target, l, triplets):
            r = len(nums) - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == target:
                    triplets.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # check if the cur l-idx val is the same as the previous one
                    # we check l-1 since we just incremented l by 1
                    while l < r and nums[l] == nums[l-1]: # l < len(nums) also works
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # r >= 0 also works
                        r -= 1
                elif tmp < target:
                    l += 1
                else:
                    r -= 1
                    
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue # skip the duplicated numbers
            helper(nums, -nums[i], i+1, triplets)
        return triplets
    


    ##### using twoSum
    # T: O(n^2), O(n) for first number and O(n) for twoSum
    # S: O(n) for hashset
    def threeSum0(self, nums: List[int]) -> List[List[int]]:

        def twoSum(i): # current idx
            seen = set() # keep track of seen numbers
            j = i + 1 # second number
            while j < len(nums):
                residue = -nums[i] - nums[j] # third number
                if residue in seen:
                    res.append([nums[i], nums[j], residue])
                    while j < len(nums)-1 and nums[j] == nums[j+1]:
                        j += 1 # avoid duplicates
                seen.add(nums[j])
                j += 1
        
        res = []
        nums.sort() # to remove duplicates later
        for i in range(len(nums)):
            if nums[i] > 0:
                break # first numebr number be negavtive, since sorted
            if i == 0 or nums[i-1] != nums[i]: # avoid duplicates
                twoSum(i)
        return res


    ##### self-made verbose version
    # use set to skip already seen numbers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(cur, target):
            h = set()
            res = []
            seen = set()
            for i in range(cur+1, len(nums)):
                residue = target - nums[i]
                if residue in h and residue not in seen:
                    seen.add(residue)
                    res.append([residue, nums[i]])
                else:
                    h.add(nums[i])
            return res

        res = []
        nums.sort()
        seen = set()
        # print (nums)
        for i in range(len(nums)-2):
            target = -nums[i]
            if target not in seen:
                seen.add(target)
                res2 = helper(i, target)
                if res2:
                    for item in res2:
                        res.append(item+[nums[i]])
        return res


                
    # def threeSum(self, nums):
    #     res=[]; tmp=[]
    #     len_=len(nums)
    #     for i in range(0, len_):
    #         for j in range(i+1, len_):
    #             for k in range(j+1, len_):
    #                 if nums[i]+nums[j]+nums[k]==0:
    #                     a=[nums[i],nums[j],nums[k]]
    #                     a.sort()
    #                     if a not in res:
    #                         res.append(a)
    #     return res

obj=Solution()
print (obj.threeSum([-2,0,0,2,2]))
