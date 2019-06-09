class Solution:
    # def threeSumClosest(self, nums, target):
    #     nums.sort()
    #     sums=[]
    #     for i in range(0, len(nums)-2):
    #         for j in range(i+1, len(nums)-1):
    #             for k in range(j+1, len(nums)):
    #                 sums.append(nums[i]+nums[j]+nums[k])
    #     least=1e10;final=0
    #     for val in sums:
    #         if abs(val-target)<least:
    #             least=abs(val-target)
    #             final=val
    #     return final
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
        return result


obj=Solution()
print (obj.threeSumClosest([0,2,1,-3],1))
