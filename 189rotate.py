'''
keys:
Solutions:
Similar:
T:
S:
'''



class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        print (nums)

    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

    def rotate1(self, nums, k):
        n = len(nums)

        cntRotated = 0
        start = 0
        curr = 0
        numToBeRotated = nums[0]
        tmp = 0
        '''Keep rotating the elements until we have rotated n 
        different elements'''
        while (cntRotated < n):
            while (curr != start):
                tmp = nums[(curr + k)%n]
                nums[(curr+k)%n] = numToBeRotated
                numToBeRotated = tmp
                curr = (curr + k)%n
                cntRotated += 1
            '''
            // Stop rotating the elements when we finish one cycle,
            // i.e., we return to start.'''

            # Move to next element to start a new cycle.
            start += 1
            curr = start
            numToBeRotated = nums[curr]

obj = Solution()
obj.rotate([1,2,3,4,5,6,7], 3)

