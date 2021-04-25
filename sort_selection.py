'''

swap the mininum to the front
'''


# T: O(n^2)
# S: O(1)

def selectionSort(array):

	for i in range(len(array)):
	    # Find the minimum element in remaining 
	    # unsorted array
	    min_idx = i
	    for j in range(i+1, len(array)):
	        if array[min_idx] > array[j]:
	            min_idx = j
	              
	    # Swap the found minimum element with 
	    # the first element        
	    array[i], array[min_idx] = array[min_idx], array[i]



def selectionSort(array):
    # Write your code here.
    curIdx = 0
	n = len(array)
	while curIdx < n - 1:
		minIdx = curIdx
		for i in range(curIdx+1, n):
			if array[i] < array[minIdx]:
				minIdx = i
		array[curIdx], array[minIdx] = array[minIdx], array[curIdx]
		curIdx += 1
	return array
				