'''
keys: sort and index
Solutions:
Similar:
T: O(N lg N)
S: O(1)
'''
import heapq
from typing import List
import random



class Solution:
    ##########
    # some solution, left partition small version, recommended
    # https://www.youtube.com/watch?v=zyskis1Gw0c
    # T: O(N) on average and O(N^2) the worst
    # S: O(1) for S.
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        # partition on the numbers in [left, right]
        left, right = 0, len(nums)-1
        #  i.e., 1-st largest is 5-th smallest, given N = 5
        targetK = len(nums) - k + 1 # l-th smallest number
        while True:
            # pos + 1 is the k-th largest element
            # pos means number of "pos" elements smaller
            pivotIdx = self.partition1(nums, left, right) # pivot
            if pivotIdx + 1 == targetK:
                return nums[pivotIdx]
            elif targetK < pivotIdx + 1:
                right = pivotIdx - 1
            else:
                left = pivotIdx + 1
    
    # reduces the size of the problem by approximately one half after 
    # each partition
    def partition1(self, nums, left, right):
        pivot = right # use the rightmost one as pivot
        # slow is the threshold dividing two partitions
        slow, fast = left, left
        while fast < pivot:
            # skip those large values since they are on the right side of slow
            if nums[fast] > nums[pivot]: 
                fast += 1
            else:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1 # 
                fast += 1 # move fast further
        # end of while, slow reaches to the end of subarray, i.e., fast == pivot
        nums[slow], nums[pivot] = nums[pivot], nums[slow]
        return slow
    
    
    ##########
    # some solution, left partition large version, right partition small
    def findKthLargest0(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        
        left, right = 0, len(nums)-1
        while True:
            # pos + 1 is the k-th largest element
            # pos is the position, thus smaller than 1
            pos = self.position(nums, left, right) # pivot
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                right = pos - 1
            else:
                left = pos + 1
    
    # reduces the size of the problem by approximately one half after 
    # each partition
    def position(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot: l += 1
            if nums[r] <= pivot: r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
            
    
    ##########
    # official quick select
    def findKthLargest1(self, nums, k):

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between [left,right], inclusive
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)
    
    
    ##########
    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
   		# convert the kth largest to (N-k+1)-th smallest
   		return self.findKthSmallest(nums, len(nums)+1-k)
   
    def findKthSmallest(self, nums, k):
   		if nums:
   			pos = self.partition(nums, 0, len(nums)-1)
   			if k > pos+1:
   				return self.findKthSmallest(nums[pos+1:], k-pos-1)
   			elif k < pos+1:
   				return self.findKthSmallest(nums[:pos], k)
   			else:
   				return nums[pos]
   
   	# choose the right-most element as pivot
    def partition(self, nums, l, r):
   		low = l
   		while l < r:
   			if nums[l] < nums[r]:
   				nums[l], nums[low] = nums[low], nums[l]
   				low += 1
   			l += 1
   		nums[low], nums[r] = nums[r], nums[low]
   		return low
    
    
    ##########
    # T: O(NogN)
    def kthLargest(self, nums, k):
        return sorted(nums)[len(nums)-k]

    
    ##########
	# O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
					# exchange elements, time consuming
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]


    ##########
	# O(nk) time, selection sort idea
    def findKthLargest3(self, nums, k):
        for i in range(len(nums), len(nums)-k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[len(nums)-k]


    ##########
	# The time complexity of adding an element in a heap of size k is 
    # O(logk), and we do it N times that means O(Nlogk) time complexity 
    # for the algorithm.
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)


    ##########
	# O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]

	
    
sol = Solution()
print (sol.findKthLargest0([3,2,1,5,6,4], 2))
