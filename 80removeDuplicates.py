'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

import collections
class Solution:
    # overwrite, T: O(N), S: O(1)
    def removeDuplicates3(self, nums):
        # Initialize the counter and the second pointer.
        j, count = 1, 1
        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):
            # If the current element is a duplicate, 
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                nums[j] = nums[i]
                j += 1  
        return j
    
    
    # poping unwanted; T: O(N^2); S: O(1)
    def removeDuplicates2(self, nums):
        # Initialize the counter and the array index.
        i, count = 1, 1
        # Start from the second element of the array and process
        # elements one by one.
        while i < len(nums):  
            # If the current element is a duplicate, 
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1        
                # If the count is more than 2, this is an
                # unwanted duplicate element and hence we 
                # remove it from the array.
                if count > 2:
                    nums.pop(i)  # this is O(N) operation     
                    # Note that we have to decrement the
                    # array index value to keep it consistent
                    # with the size of the array.
                    i-= 1         
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            # Move on to the next element in the array
            i += 1    
        return len(nums)
    
    
    def removeDuplicates1(self, nums):
        count=collections.defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]]+=1
            if count[nums[i]]>2:
                nums[i]=-1
        nums.remove(-1)
        return nums


    def removeDuplicates(self, nums):
        i=0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i

obj=Solution()
print(obj.removeDuplicates([1,1,1,2,2,3]))
