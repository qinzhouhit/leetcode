'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
'''
Given an array of numbers sorted in ascending order, find the element in the array 
that has the minimum difference with the given ‘key’.
'''

def search_min_diff_element(arr, target):
	if target < arr[0]:
		return arr[0]
	if target > arr[-1]:
		return arr[-1]
	n = len(arr)
	l, r = 0, n-1
	while l <= r:
		mid = l + (r - l) // 2
		if target < arr[mid]:
			r = mid - 1
		elif target > arr[mid]:
			l = mid + 1
		else:
			return arr[mid]

	# at the end of the while loop, 'start == end+1'
		# we are not able to find the element in the given array
		# return the element which is closest to the 'key'
		# --------arr[l]--target-----------arr[r]----------------
		if abs(target - arr[l]) < abs(target - arr[r]): # closer to arr[l]
			return arr[l]
		return arr[r]

print(search_min_diff_element([4, 6, 10], 7))
# print(search_min_diff_element([4, 6, 10], 4))	
# print(search_min_diff_element([1, 3, 8, 10, 15], 12))
# print(search_min_diff_element([4, 6, 10], 17))
