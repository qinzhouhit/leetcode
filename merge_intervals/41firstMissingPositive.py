'''
keys: dp
Solutions:
Similar:
T: O(n)
S: O(1)
'''
from typing import List

class Solution:
    # educative.io, cyclic sort
    # O(n) for T and O(1) for S
    # Place the numbers on their correct indices and ignore all numbers
    # that are out of the range of the array
    # The true array should be [1, 2, ..., n] for nums with length n
    def firstMissingPositive3(self, nums: List[int]) -> int:
        i = 0; n = len(nums)
        while i < n:
            idx = nums[i] - 1 # e.g., nums[i] should be at idx nums[i]-1
            # the key difference is "nums[i] > 0 and nums[i] <= n"
            # ignore all numbers that are out of the range of the array
            # (i.e., all negative numbers and all numbers greater than 
            # or equal to the length of the array)
            if 0 < nums[i] <= n and nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx] # swap nums[i] to the right position
            else:
                i += 1
        for i in range(n): # return the one not in position
            if nums[i] != i+1:
                return i+1
        return n + 1 # the next one



    # hash swap
    def firstMissingPositive1(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and \
                nums[nums[i]-1] != nums[i]: # swap the element to make it 
                    # in the right position, e.g., [1,-1,3,4]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1 # the element missing
        
        return len(nums)+1 # if all things existing, then...
    
    # nice solution
    def firstMissingPositive12(self, nums: List[int]) -> int:
        """
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n
    
    
    # hash set 
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
        
sol = Solution()
print (sol.firstMissingPositive1([2,1]))
        

