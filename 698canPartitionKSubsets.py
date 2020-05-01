'''
keys:
Solutions:
Similar:
T:
S:
'''

# https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/PartitionIntoKEqualSumSubsets/PartitionIntoKEqualSumSubsets.java
class Solution:
    # the time complexity is O(k * 2^n), at least it's an upper bound.
    # Because it takes the inner recursion 2^n time to find a good subset.
    # Once the 1st subset is found, we go on to find the second, which would take
    # 2^n roughly (because some numbers have been marked as visited).
    # So T = 2^n + 2^n + 2^n + ... = k * 2^n.
    def canPartitionKSubsets(self, nums, k) -> bool:
        # corner cases
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


    def canPartitionKSubsets1(self, nums, k):
        # sort and try the bigger values in the buckets
        # each time, try fill the nums[pos] in the buckets with constraints
        if len(nums) < k:
            return False
        allSum = sum(nums)
        nums.sort(reverse = True) # descending
        if allSum % k: return False
        target = [allSum/k] * k

        def dfs(pos):
            if pos == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    target[i] += nums[pos]
            return False
        return dfs(0)


obj = Solution()
print (obj.canPartitionKSubsets1([4, 3, 2, 3, 5, 2, 1], 4))



