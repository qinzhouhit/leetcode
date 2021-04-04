'''
keys:
Solutions:
Similar: 987
T:
S:
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# in 314, the order should be from left to right
# in 987, the order should be decided by node value

class Solution:
    # O(N) for S and T
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

    # easy to avoid the sorting, use max_ and min_
    # BFS; T: O(NlogN); S: O(N), N as number of nodes in the tree
    def verticalOrder(self, root):
        if not root: return []

        import collections
        queue = collections.deque([(root, 0)])
        res = collections.defaultdict(list)
        while queue:
            node, col = queue.popleft()
            if node:
                res[col].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1)) # left column
                if node.right:
                    queue.append((node.right, col + 1)) # right column
        # sorted(res): return the sorted keys (ascending)
        return [res[i] for i in sorted(res)]





        
