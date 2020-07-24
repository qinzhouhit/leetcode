'''
keys: 
Solutions:
Similar:340
T:
S:
'''
from typing import List


class Solution:
    # shorter, prefix sum
    # whenever the sums has increased by a value of k, 
    # we've found a subarray of sums=k.
    # https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        return count
    
    # hashmap
    # O(n) for S and T
    '''
    // Sliding window -- No, contains negative number
        // hashmap + preSum
        /*
            1. Hashmap<sum[0,i - 1], frequency>
            2. sum[i, j] = sum[0, j] - sum[0, i - 1]    --> sum[0, i - 1] = sum[0, j] - sum[i, j]
                   k           sum      hashmap-key     -->  hashmap-key  =  sum - k
            3. now, we have k and sum.  
                  As long as we can find a sum[0, i - 1], we then get a valid subarray
                 which is as long as we have the hashmap-key,  we then get a valid subarray
            4. Why don't map.put(sum[0, i - 1], 1) every time ?
                  if all numbers are positive, this is fine
                  if there exists negative number, there could be preSum frequency > 1
        */'''
    def subarraySum1(self, nums: List[int], k: int) -> int:
        ct = 0; sums = 0
        hashmap = {}
        hashmap[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in hashmap:
                ct += hashmap[sums - k]
            hashmap[sums] = hashmap.get(sums, 0) + 1
        return ct
        
        
    
    # LTE
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = 0
        for i in range(len(nums)):
            tmp_sum = 0
            for j in range(i, len(nums)):
                tmp_sum += nums[j]
                if tmp_sum == k:
                    ct += 1
        return ct
    
    
sol = Solution()
sol.subarraySum2([1,2,1,3], 3)
