'''
keys: two pivots in two arrays, adjust the first pivot by binary fashion
Solutions:
Similar:
T: O(log(min(m,n)))
S:
'''

'''
      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
'''
# https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m+n+1)/2)
        while imin <= imax:
            i = int((imin + imax) / 2) # binary search for
            j = half_len - i
            if j > 0 and i < m and nums2[j-1] > nums1[i]: # j > 0 can be omitted
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]: # j < n can be omitted
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return max_left # m+n is odd

                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums1[i], nums2[j])

                return (max_left + min_right)/2 # m+n is even

                
obj = Solution()
print (obj.findMedianSortedArrays([1,2], [3,4]))

