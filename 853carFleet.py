""" 
keys: 
Solutions:
Similar:
T:
S:
"""



class Solution:
	# T: O(NlogN)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    	# sorted(zip(x, y)) will return a list of tuples (x1, y1), sorting by x then y
    	# i.e., sorted by increasing position in our case
    	# notice the position means there are (target-position) miles away from position
    	# each val in time corresponds to one car, by position
    	time = [(target - pos) / v for pos, v in sorted(zip(position, speed))]

    	# If another car needs less or equal time than cur_slowest,
		# it can catch up this car fleet.
    	res = cur_slowest = 0
    	for t in time[::-1]:  # time[::-1] meaning starting checking the last car from the end
    	# notice that the new lowest will never catch the prev lowest, since we are processing 
    	# cars starting from the ending positions
    		if t > cur_slowest:  
    			cur_slowest = t
    			res += 1
    	return res





