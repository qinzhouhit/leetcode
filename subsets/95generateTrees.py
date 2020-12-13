'''
keys:
Solutions:
Similar: 96
T: n*G
S: n*G, G as the Catalan number G(n) = 4^n / (n^(3/2))
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Estimated time complexity will be O(n*2^n) but the actual time complexity 
    # O(4^n/sqrt(n)) is bounded by the Catalan number and is beyond the scope of a coding interview. See more details here.


    def generateTrees(self, n: int): #  -> List[TreeNode]
        def helper(start, end):
            if start > end:
                return [None,]

            all_trees = []
            for i in range(start, end+1): # pick up a root
                # all possible left subtrees if i is chosen to be a root
                left_trees = helper(start, i-1)

                # all possible right subtrees if i is chosen to be a root
                right_trees = helper(i+1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees

        return helper(1, n) if n else []


sol = Solution()
print (sol.generateTrees(3))
