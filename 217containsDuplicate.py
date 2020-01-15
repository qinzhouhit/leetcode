class Solution:
    def containsDuplicate1(self, nums):
        # exceeded time limit
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def containsDuplicate2(self, nums):
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            if num in nums:
                return True
        return False

obj = Solution()
print (obj.containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))




