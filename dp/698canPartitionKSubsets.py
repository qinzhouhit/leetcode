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
            if not used[i] and inProgressBucketSum+nums[i] <= targetBucketSum:
                used[i] = True
                # See if we can partition from this point with the item added
                #           to the current bucket progress
                if self.canPartition(i+1, nums, used, k, inProgressBucketSum+nums[i], targetBucketSum):
                    return True
                used[i] = False
        return False



    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-Thinking-Process
    # in each iteration you check if an element should belong to the set or not and you do this K times.
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        totalSum = sum(nums)
        nums.sort(reverse = True) # descending
        if totalSum % k: return False
        visited = [False] * len(nums)
        return self.dfs(nums, k, visited, totalSum//k, 0, 0)

    # check the k-partition, cur_sum is the current subsetSum
    def dfs(self, nums, k, visited, target, cur_sum, nxtIdx):
        if k == 1: return True # since k-1 partitions are good, the remaining one is ok
        if cur_sum == target:
            return self.dfs(nums, k-1, visited, target, 0, 0)
        for i in range(nxtIdx, len(nums)):
            if not visited[i] and cur_sum+nums[i] <= target:
                visited[i] = True
                if self.dfs(nums, k, visited, target, cur_sum+nums[i], i+1):
                    return True
                visited[i] = False
        return False

        


    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108741/Solution-with-Reference
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # sort and try the bigger values in the buckets
        # each time, try fill the nums[pos] in the buckets with constraints
        ''' O(k N−k k!), where N is the length of nums, and k is as given. As we 
        skip additional zeroes in groups, naively we will make O(k!)O(k!) calls to
         search, then an additional O(k^{N-k}) calls after every element
        of groups is nonzero. Space Complexity: O(N), the space used by 
        recursive calls to search in our call stack. '''
        if len(nums) < k:
            return False
        totalSum = sum(nums)
        nums.sort(reverse = True) # descending
        if totalSum % k: return False
        target = [totalSum//k] * k

        def dfs(idx):
            if idx == len(nums):
                return True # why? even there are values left in target?
            for i in range(k):
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if dfs(idx+1):
                        return True
                    target[i] += nums[idx]
            return False
        return dfs(0)


obj = Solution()
print (obj.canPartitionKSubsets1([4, 3, 2, 3, 5, 2, 1], 4))



