'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# work backwards with modulo
	# T: O(log(max(tx, ty)))
	# S: O(1)
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else: # tx < ty
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy 


	# work backwards
	# T: O(max(tx, ty))
	# S: O(1)
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		while tx >= sx and ty >= sy:
			if tx == sx and ty == sy:
				return True
			if tx > ty:
				tx -= ty
			else:
				ty -= tx
		return False



	# dp
	# S and T: O(tx * ty)
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		seen = set()

		def helper(x, y):
			if (x, y) in seen:
				return
			if x > tx or y > ty:
				return 
			seen.add((x, y))
			helper(x+y, y)
			helper(x, x+y)

		helper(sx, sy)
		return (tx, ty) in seen



	# T: O(2^(tx+ty))
	# S: O(tx * ty) for call stack
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        if sx == tx and sy == ty:
            return True
        return self.reachingPoints(sx+sy, sy, tx, ty) or self.reachingPoints(sx, sx+sy, tx, ty)


