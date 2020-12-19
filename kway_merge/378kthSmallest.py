'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

from heapq import *

class Solution:
    
    # binary search, official
    # T: O(N*log(max - min)), max and min of the matrix, for each iteration we 
    # take O(N) for counting
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, row_num = 0, len(matrix)
        row, col = row_num - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
            # As matrix[row][col] is bigger than the mid, let's keep track
            # of the smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
            # As matrix[row][col] is less than or equal to the mid, let's 
            # keep track of the biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1 # all the numbers in the prev column smaller than middle
                col += 1
        return count, smaller, larger
    
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) // 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
            # smaller: largest number smaller than the middle
            # larger: smallest number greater than the middle
            # count: number of elements less than or equal to the middle
            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower
        return start
    
    # heapq
    # The heap data structure gives us O(1) access to the minimum element and 
    # log(N) removal of the minimum element and addition of a new one.
    # X = min(N, K), T: O(X + KlogX), S: O(X) for heap
    # construction of heapq takes O(X) time, N as number of rows
    # K iteration, with each extracting the min element from a heap with X elements
    def kthSmallest1(self, matrix, k):
        minHeap = []
    
        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k, len(matrix))): # clear range choice
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
    
        # take the smallest(top) element form the min heap, if the running 
        # count is equal to k' return the number. If the row containing  the top 
        # element has more elements, add the next element to the heap
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i+1:
                heappush(minHeap, (row[i+1], i+1, row))
        return number
    
    
    # brute force
    def kthSmallest(self, matrix, k):

        # self-made, NlogN
        if not matrix or not matrix[0]:
            return None

        vals = [v for row in matrix for v in row ]
        vals.sort()
        # print (vals)
        return vals[k-1]




