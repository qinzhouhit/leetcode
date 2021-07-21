"""
keys: 
Solutions:
Similar:
T:
S:
"""

class Solution:
	# the time index starts at 1, not 0
	# https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])  # start time
        i = 0
        h = []
        time = tasks[0][0]  # set current time
        while len(res) < len(tasks):  # break when all tasks processed
        	while i < len(tasks) and tasks[i][0] <= time:  # push all tasks with passed starting time
        		heapq.heappush(h, (tasks[i][1], tasks[i][2]))  # processing_time, original_idx
        		i += 1
        	if h:
        		t_diff, original_idx = heapq.heappop(h)  # the shortest processing_time
        		time += t_diff
        		res.append(original_idx)
        	elif i < len(tasks):  # h empty, let the CPU sit idle
        		# until the next task in the task list is ready to be pushed into the heap.
        		time = tasks[i][0]
       	return res

