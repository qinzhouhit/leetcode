'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times 
around a pivot, find ‘k’.
You can assume that the array does not have any duplicates.

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
'''

# we are asked to find the index of the minimum element.

def count_rotations(arr):
	l, r = 0, len(arr) - 1
	while l < r:
		mid = l + (r - l) // 2
		if mid < r and arr[mid] > arr[mid + 1]: # mid is greater than the next
			return mid + 1
		if mid > l and arr[mid] < arr[mid - 1]: # mid is greater then the previous
			return mid

		if arr[l] < arr[mid]: # left subarray is ascending
			l = mid + 1 # find in the right part
		else:
			r = mid - 1
	# print (l, r)
	return 0 # l = r + 1

# print(count_rotations([10, 15, 1, 3, 8])) # 2
# print(count_rotations([4, 5, 7, 9, 10, -1, 2])) # 5
# print(count_rotations([1, 3, 8, 10])) # 0


# similar one: find the rotation count of a sorted and rotated array that
#  has duplicates too?
def count_rotations_with_duplicates(arr):
	l, r = 0, len(arr) - 1
	while l < r:
		mid = l + (r - l) // 2
		if mid < r and arr[mid] > arr[mid + 1]:
			return mid + 1
		if mid > l and arr[mid] < arr[mid - 1]:
			return mid # not sure if this part is necessary
	# below: difference comapred to the previous version
	# the best we can do is to skip one number from both ends if they are not 
	# the smallest number
	if arr[l] == arr[mid] == arr[r]:
		print (arr[l], arr[mid], arr[r])
		if arr[l] > arr[l + 1]: # arr[l] is not the smallest
			return l + 1
		l += 1
		if arr[r - 1] > arr[r]:
			return r
		r -= 1
	# left side is sorted, so the pivot is on right side
	elif arr[l] < arr[mid] or (arr[l] == arr[mid] and arr[mid] > arr[r]):
		l = mid + 1
	else: # right side is sorted, so the pivot is on the left side
		r = mid - 1
	return 0 # not rotated

print(count_rotations_with_duplicates([3, 3, 7, 3]))











	