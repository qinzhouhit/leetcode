'''

move the smaller values to the front
'''




# T: O(n^22)
# S: O(1)
def insertionSort(array):
    # Write your code here.
	
	for i in range(1, len(array)):
		j = i 
		while j > 0 and array[j-1] > array[j]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array
    



def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        val = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than val, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and val < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = val