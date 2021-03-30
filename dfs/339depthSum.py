'''
keys: stack
Solutions:
Similar:
T:
S:
'''

class Solution:
    # T: O(N), N as the total number of nested elements in the input list.
    # S: O(D), D as the maximum level of nesting in the input. worst case as O(N)
    # iterative dfs
	def depthSum(self, nestedList: List[NestedInteger]) -> int:
		if not nestedList:
            return 0
        
        stack = []
        res = 0
        for item in nestedList:
            stack.append([item, 1])
        while stack:
            nxt, depth = stack.pop()
            val = nxt.getInteger()
            if val is not None:
                res += depth * val
            else:
                for item in nxt.getList():
                    stack.append([item, depth+1])
        return res
        
    # dfs recursion
    def depthSum1(self, nestedList: List[NestedInteger]) -> int:

    	def dfs(alllists, depth):
    		res = 0
    		for item in alllists:
    			if item.isInteger():
    				res += item.getInteger() * depth
    			else:
    				res += dfs(item.getList(), depth+1)
    		return res

    	return dfs(nestedList, 1)

   	# bfs iteration
    def depthSum2(self, nestedList: List[NestedInteger]) -> int:
    	queue = deque(nestedList)
    	depth = 1
    	res = 0
    	while queue:
    		for _ in range(len(queue)): 
    			item = queue.popleft()
    			if item.isInteger():
    				res += depth * item.getInteger()
    			else:
    				queue.extend(item.getList()) # extend!!! like unpacking/flatten
    		depth += 1
    	return res

