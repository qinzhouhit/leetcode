'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # O(MN) for S and T
    def wallsAndGates1(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        row, col = len(rooms), len(rooms[0])
        # find the index of all gates
        q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]
        for x, y in q:
            # get the distance from a gate， pre-calculated for next move
            distance = rooms[x][y]+1 
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                # find the INF around the gate
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < row and 0 <= new_y < col and \
                        rooms[new_x][new_y] == 2147483647:
                    # update the value
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y)) # to find empty rooms around these empty rooms
					# if empty room cannot be reached by this way, then it is impossible
					# to find a gate to this empty room
# 		print (rooms)
                    
                    
    # like number of islands
    # T: O((MN)^2)
    def wallsAndGates1(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not any(rooms):
            return None

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, dist):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] < dist:
            return
        rooms[i][j] = dist
        for dx, dy in [[-1,0],[1,0], [0,-1], [0,1]]:
            self.dfs(rooms, i + dx, j + dy, dist + 1)



	

obj = Solution()
obj.wallsAndGates([[2147483647,  		-1,			0,2147483647],
					[2147483647,2147483647,2147483647,   	  -1],
					[2147483647,		-1,2147483647,		  -1],
					[		  0,		-1,2147483647,2147483647]])
