'''
keys: backtracking and DP
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # TODO: HashSet and Intelligent Sequence Building
    # based on the brutal force, use set
    # T: O(n+n), O(n) for for loop and O(n) for while loop
    # S: O(n) for the set
    def longestConsecutive2(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # attempt to build sequences from numbers that are not already part of a longer
            # sequence. first ensuring that the number that would immediately precede the 
            # current number in a sequence is not present
            if num - 1 not in num_set: # genius step... so we can skip lots of cases
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


    # TODO: sorting
    # T: O(nlogn)
    # S: O(1) or O(n) for the sorted array
    def longestConsecutive1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # if they are equal, we just continue since equality does not
            # affect the streak, e.g., [-1, -1, 0, 1], just move to the 2nd -1
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        # becuase the current_streak (w/ last element) may be the longest
        return max(longest_streak, current_streak)
        # return longest_streak

    # TODO: brutal force
    # T: O(n^3): outer loop//current_num incremented by 1//O(n) lookup for "in" the array
    # S: O(1) for those integer variables
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


sol = Solution()
print (sol.longestConsecutive2([9,1,4,7,3,-1,0,5,8,-1,6]))
