'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# T: O(N), S: O(1)
'''
It's a limit cycle trajectory if the robot is back to the center: x = y = 0 or 
if the robot doesn't face north: idx != 0.
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L": # facing west
                idx = (idx + 3) % 4
            elif i == "R": # facing east
                idx = (idx + 1) % 4
            else: # "G"
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0

        # if x == 0 and y == 0: return True
        # if idx == 0: return False
        # return True # other cases, where it goes to origin after 4 circles