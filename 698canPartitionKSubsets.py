'''
keys:
Solutions:
Similar:
T:
S:
'''

# https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/PartitionIntoKEqualSumSubsets/PartitionIntoKEqualSumSubsets.java
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)

        if k <= 0 or k > len(nums) or (totalSum % k):
            return False

        return self.canPartition(0, nums, [False]*len(nums), k, 0, totalSum/k)

    def canPartition(self, iterationStart, nums, used, k, inProgressBucketSum, targetBucketSum):
        # we don't have to fill the last bucket when done with k-1
        if k == 1: return True
        # one bucket full, k-> k-1
        if inProgressBucketSum == targetBucketSum:
            return self.canPartition(0, nums, used, k-1, 0, targetBucketSum)

        for i in range(iterationStart, len(nums)):
            if not used[i] and inProgressBucketSum+nums[i]<=targetBucketSum:
                used[i] = True
                # See if we can partition from this point with the item added
                #           to the current bucket progress
                if self.canPartition(i+1, nums, used, k, inProgressBucketSum+nums[i], targetBucketSum):
                    return True
                used[i] = False
        return False


