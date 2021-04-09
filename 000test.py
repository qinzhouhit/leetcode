from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        def helper(cur, target):
            h = set()
            res = []
            for i in range(cur+1, len(nums)):
                residue = target - nums[i]
                if residue in h:
                    res.append([residue, nums[i]])
                else:
                    h.add(nums[i])
            return res

        res = []
        nums.sort()
        seen = set()
        print (nums)
        for i in range(len(nums)-2):
            target = -nums[i]
            if target not in seen:
                seen.add(target)
                res2 = helper(i, target)
                if res2:
                    for item in res2:
                        res.append(item+[nums[i]])
        return res

obj = Solution()
print (obj.threeSum([-1,0,1,2,-1,-4]))



