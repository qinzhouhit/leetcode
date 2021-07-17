""" 
keys: 
Solutions:
Similar:
T:
S:
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	# https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution
	# If a node is root (has no parent) and isn't deleted,
	# then we add it to the result.
	# T: O(N)
	# S: O(H + N), H as the height of tree
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    	to_delete = set(to_delete)

    	def helper(node, is_root):
    		if not node:
    			return None  
    		node_deleted = node.val in to_delete  # boolean
    		if is_root and not node_deleted:
    			res.append(node)  # this node not deleted
    		node.left = helper(node.left, node_deleted)  # node deleted means node.left being root
    		node.right = helper(node.right, node_deleted)
    		return None if node_deleted else node

    	res = []
    	helper(root, True)
    	return res


    # not so clean version
    # https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res




