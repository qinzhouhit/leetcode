'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
 Though we know that the array is sorted, we don’t know if it’s sorted in ascending or 
 descending order. You should assume that the array can have duplicates.
'''

# educative.io version, sorted but no idea ascending or descending
# O(logN) for T and O(1) for S
def binary_search(arr, key):
	l, r = 0, len(arr) - 1
	isAscending = arr[l] < arr[r]
	while l <= r:
		mid = l + (r - l) // 2
		if arr[mid] == key:
			return mid
		if isAscending:
			if arr[mid] < key:
				l = mid + 1
			else:
				r = mid - 1
		else:
			if arr[mid] < key:
				r = mid - 1
			else:
				l = mid + 1
	return -1
