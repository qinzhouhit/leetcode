'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


'''
Queue.PriorityQueue is a thread-safe class, while the heapq module makes 
';no thread-safety guarantees. 
'''

class Solution:
	# heapq
	'''
	Time: O(nlogn). At most nn elements are added to the queuequeue. 
	Adding each element is followed by heapification, which takes O(logn) time.
	Space: O(n). The queuequeue containing the durations of the courses 
	taken can have atmost nn elements
	'''
	def scheduleCourse(self, courses: List[List[int]]) -> int:
		courses.sort(key=lambda x: (x[1])) # ending date
        q = []
        time = 0
        for c in courses:
            if time + c[0] <= c[1]:
                heappush(q, -c[0]) # max heap
                time += c[0]
            elif q and q[0] < -c[0]: # greedy, alway keep the less time costly course
                time += c[0] + heappop(q)
                heappush(q, -c[0])
        return len(q)



	# T and S: O(n*d), n as number of courses and d as 
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        def helper(courses, i, time, memo):
            # i for course idx, time for the current cumulative time
            if i == courses_num:
                return 0
            if memo[i][time]:
                return memo[i][time]
            taken = 0
            if time + courses[i][0] <= courses[i][1]: # 
                taken = 1 + helper(courses, i+1, time + courses[i][0], memo)
            not_taken = helper(courses, i+1, time, memo)
            memo[i][time] = max(taken, not_taken)
            return memo[i][time]

        courses.sort(key=lambda x: (x[1])) # ending date
        courses_num = len(courses)
        last_date = courses[courses_num-1][1] # last closing date
        memo = [[0] * (last_date+1) for _ in range(courses_num)]
        return helper(courses, 0, 0, memo)