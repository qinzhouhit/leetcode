'''
keys:
Solutions:
Similar:
T:
S:
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# T: O(|s| * |t|)
    # https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		def isMatch(s, t):
			if (s is None and t is not None) or (s is not None and t is None):
				return False
			elif s is None and t is None:
				return True

			if s.val == t.val:
				if isMatch(s.left, t.left) and isMatch(s.right, t.right):
					return True
				else:
					return False

		if isMatch(s, t):
			return True
		if s is None:
			return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution2:
	# compare nodes
	# T: O(m*n), worst case as skewed tree
	# S: O(n), depth of recursion tree, n as the # of nodes in s
	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		return self.traverse(s, t)

	def equals(self, x, y):
		if (x == None and y == None):
			return True
		if (x == None or y == None):
			return False
		return x.val == y.val and self.equals(x.left, y.left) and\
	self.equals(x.right, y.right)

	def traverse(self, s, t):
		return s != None and (self.equals(s, t) or self.traverse(s.left, t)\
							  or self.traverse(s.right, t))


class Solution1:
	# transform into string, any traverse order should work
	# T: O(m^2 + n^2 + m*n), n nodes in s and m nodes in t
	# S: O(max(m, n)), depth for recursion
	
	# def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
	# 	tree1 = self.preorder(s, True)
	# 	tree2 = self.preorder(t, True)
	# 	return (tree2 in tree1) # takes O(m*n)?
	#
	# def preorder(self, root, left):
	# 	if root == None:
	# 		# if left:
	# # 			# 	return 'lnull'
	# # 			# else:
	# # 			# 	return 'rnull'
	# 		return 'null'
	# return '#'+str(root.val)+' '+self.preorder(root.left, True)+' '+self.preorder(root.right, False)

	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		tree1 = self.preorder(s)
		tree2 = self.preorder(t)
		return (tree2 in tree1) # takes O(m*n)?

	def preorder(self, root):
		if root == None:
			return 'null'
		return '#'+str(root.val)+' '+self.preorder(root.left)+' '+self.preorder(root.right)
