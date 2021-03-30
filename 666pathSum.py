'''
keys: 
Solutions:
Similar: 
T: 
S: 
'''
from typing import List



class Solution:
	# https://leetcode.com/problems/path-sum-iv/discuss/121742/Python-easy-to-understand-with-comments
	# O(N) for S and T
    def pathSum(self, nums: List[int]) -> int:
    	dic = collections.defaultdict(int)
        for num in nums:
        	depth, pos, val = num//10, num//10%10, num%10
        	# At each level, store the sum of all the previous nodes covered
        	dic[(depth, pos)] += dic[(depth-1, (pos+1)//2)] + val # nice (pos+1)//2

        res = 0
        for depth, pos in dic.keys():
        	# Since the leaf nodes contain sum of the entire path 
        	# from root to each leaf nodes, just check whether it is 
        	# a leaf node or not and then add up all the leaf nodes
        	if (depth+1, pos*2-1) not in dic and (depth+1,pos*2) not in dic:
                res += dic[depth, pos]
        return res



    # construct the tree
    # O(N) for S and T
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, nums):
        self.ans = 0
        root = Node(nums[0] % 10)

        for x in nums[1:]:
            depth, pos, val = x//100, x//10 % 10, x % 10
            pos -= 1 # idx reset as 0
            cur = root
            for d in range(depth - 2, -1, -1):
                if pos < 2**d: # d=1, # nodes=1=2^0; d=2, # nodes=2^1
                '''
                if not cur.left:
				....cur.left = Node(val)
				cur = cur.left
                '''
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur = cur.right or Node(val)

                pos %= 2**d # 

        def dfs(node, running_sum = 0):
            if not node: return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans
            


