'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


'''
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered 
bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically
 increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
'''

# first, find the index of maximum num
# binary search in two arrays to search the key


def search_bitonic_array(arr, key):
	maxIdx = find_max(arr)
	keyIdx = binary_search(arr, key, 0, maxIdx)
	if keyIdx != -1:
		return keyIdx
	return binary_search(arr, key, maxIdx+1, len(arr)-1)

def binary_search(arr, key, l, r):
	while l <= r:
		mid = l + (r - l) // 2
		if key == arr[mid]:
			return mid
		if arr[l] < arr[r]: # ascending order
			if key > arr[mid]:
				l = mid + 1
			else:
				r = mid - 1
		else:
			if key > arr[mid]:
				r = mid - 1
			else:
				l = mid + 1
	return -1

def find_max(arr): # remember this template for bitonic array
	l, r = 0, len(arr) - 1
	while l < r:
		mid = l + (l - r) // 2
		if key > arr[mid]:
			l = mid + 1
		else:
			r = mid
	return l
