'''
keys: two pointer
Solutions:
Similar:
T: O(n^2)
S: O(1) for res
'''


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # We do not need to consider i after nums[i]>0,
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
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # exclude possible duplicate triplets
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
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
