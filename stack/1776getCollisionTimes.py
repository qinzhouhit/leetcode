""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	# https://leetcode.com/problems/car-fleet-ii/discuss/1085844/Python3.-Simple-solution-with-using-stack
	def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        # maintain cars that might collide with current car
        # their collision time is increasing
        stack = []
        for position, speed in cars[::-1]:
            # if current car speed is less than the head of the stack then there won't be a collision
            # or if c1 collides with c2 after c2 collides with c3, we can ignore c2 and find collision
            # time of c1 and c3 instead
            # (where c1 is current car, c2 is the head of the stack and c3 is the car that c2 will collide with)
            # (if we have [[x1, s1], [x2, s2]], then collision time is (x2 - x1) / (s1 - s2))
            while stack and (speed <= stack[-1][1] or \
            		(stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()  # pop c2
            # if stack is empty, then current car will never collide with the next car
            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            # find collision time and add the car to the stack
            # for non-collision cases, they are popped out during the while loop
            else:
                collideTime = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collideTime))
                result.append(collideTime)
        result.reverse()
        return result


	"""
	# https://leetcode.com/problems/car-fleet-ii/discuss/1085987/JavaC%2B%2BPython-O(n)-Stack-Solution
	# O(N) for S and T

	We care about the collision time of the cars in front us.
	We iteratre from the last to the first car,
	and we maintain a stack of car indices,
	where their collision time is strict decreasing.

	Imagine a,b,c on the road
	if the a catches b later than b catched c,
	then a won't catch b but catch b+c instead.
	"""
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
    	stack = []
        n = len(cars)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = cars[i]  # position, speed
            while stack and (s <= cars[stack[-1]][1] or \
            	(cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        return res
