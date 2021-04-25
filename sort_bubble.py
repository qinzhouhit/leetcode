'''
move the large values to the end
'''

# T: O(n^2) even when the array is sorted
# S: O(n)
def bubbleSort(array):
    # Write your code here.
    n = len(array)
	for i in range(n):
		for j in range(0, n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				
	return array