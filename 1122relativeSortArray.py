'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    	arr2order = {val:idx for idx, val in enumerate(arr2)}
    	# since 1 <= len(arr1), len(arr2) <= 1000
        res = sorted(arr1, key=lambda x: arr2order.get(x, x+1000))
        return res


    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
    	ct = [0] * 1001
    	for val in arr1:
    		ct[val] += 1
    	i = 0
    	for val in arr2:
    		while ct[val] > 0:
    			ct[val] -= 1
    			arr1[i] = val
    			i += 1
    	# those number of arr1 not in arr2
    	for val in range(len(ct)):
    		while ct[val] > 0:
    			ct[val] -= 1
    			arr1[i] = val
    			i += 1
    	return arr1

