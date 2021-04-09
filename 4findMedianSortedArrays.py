'''
keys: two pivots in two arrays, adjust the first pivot by binary fashion
Solutions:
Similar:
T: O(log(min(m,n)))
S:
'''

'''
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
Partition the two arrays so taht left part and right part have the same number of nums
A is partitioned at idx i-1; B is partitioned at j-1 and the nums in left part is less 
than the nums in the right part. 
As for how the elements are sorted within each part, we DONT care!
Once we find the partition, then A[i-1], A[i], B[j-1], B[j] are the only elements we care!
We have to make sure taht A[i-1] <= B[j] and B[j-1] <= A[i]
      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

If odd total nums, left part will have one more element than right part
If even, then they have the same nums
'''
# https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        if len2 == 0: # since len2 is the larger one
            raise ValueError

        # i the partition idx of nums1
        # left1, right1 are the ptrs in binary search of nums1
        left1, right1, half_len = 0, len1, (len1+len2+1)//2
        while left1 <= right1:
            i = (left1 + right1) // 2 # mid idx of binary search for nums1
            # partition of nums2, just to make sure left and right parts 
            # have the same number of nums
            j = half_len - i 
            if i < len1 and j > 0 and nums2[j-1] > nums1[i]: # j > 0 can be omitted
                # i is too small, must increase it
                left1 = i + 1
            elif i > 0 and j < len2 and nums1[i-1] > nums2[j]: # j < n can be omitted
                # i is too big, must decrease it
                right1 = i - 1
            else: # perfect partition for nums1
                # i == 0 means all nums1 are right part
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])

                if (len1+len2) % 2 == 1:
                    return max_left # m+n is odd

                if i == len1: min_right = nums2[j] # i == len1, means all nums1 are on the left part
                elif j == len2: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left + min_right)/2 # m+n is even


    ##### naive self-made O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            nums1, nums2 = nums2, nums1
        
        arr = []
        i, j = 0, 0 # the smaller one
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1
        while j < len(nums2):
            arr.append(nums2[j])
            j += 1
        # print (arr)
        n = len(arr)
        if n % 2:
            return arr[n//2]
        else:
            return (arr[n//2-1]+arr[n//2])/2
                
            
        
                
obj = Solution()
print (obj.findMedianSortedArrays([1,2], [3,4]))












