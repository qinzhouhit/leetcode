'''
ignore this one, problematic
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # TODO: two pointers/ start from the end. T: O(n+m), S: O(1)
    def merge3(self, nums1, m, nums2, n):
        p1 = m-1; p2 = n-1
        p = m+n-1 # pointer for nums1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:# add missing elements from nums2
                nums1[:p2 + 1] = nums2[:p2 + 1]
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2, e.g., [2,3,3,0,0,0,0] [1,6,7,8]
        # 1 will be left
        # numbers in nums1 won't be left since they remain still in nums1 if they are smaller
        # than all numbers in nums2, or they will be placed in later part of nums1
        # if they are somehow larger than numbers in nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]



    # TODO: two pointers. T: O(n+m), S: O(m)
    def merge2(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []
        ptr1 = 0; ptr2 = 0
        while ptr1 < m and ptr2 < n:
            if nums1_copy[ptr1] < nums2[ptr2]:
                nums1.append(nums1_copy[ptr1])
                ptr1 += 1
            else:
                nums1.append(nums2[ptr2])
                ptr2 += 1
        if ptr1 < m:
            nums1[ptr1+ptr2:] = nums1_copy[ptr1:]
        if ptr2 < n:
            nums1[ptr1+ptr2:] = nums2[ptr2:]

    # TODO: just sort. T: O((n+m)log(n+m)), S: O(1)
    def merge1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[n:]

        print (nums1)

obj=Solution()
obj.merge([0],0,[1],1)

