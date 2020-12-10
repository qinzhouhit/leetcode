'''
keys: bfs+queue or dfs+stack
Solutions:
Similar: 102
T: O(n) n: number of nodes
S:
'''

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # educative.io version, same as 102 except use deque for res
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        result = deque()
        if not root: return result
        # TODO: Write your code here
        q = deque([root])
        while q:
            lvl_size = len(q)
            lvl_vals = []
            for _ in range(lvl_size):
                node = q.popleft()
                lvl_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.appendleft(lvl_vals)
        return result

    # bfs + queue
    def levelOrderBottom(self, root):
        from collections import deque
        if not root:
            return []
        queue, res = deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                # left first, since left will be popped
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res[::-1]


    # dfs + stack
    def levelOrderBottom2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1)) # left! To be popped firstly
        return res


    # bfs + queue
    def levelOrderBottom3(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1)) # left! to be popped firstly
                queue.append((node.right, level+1))
        return res


    def levelOrder(self, root):
        ret = []
        level = [root]
        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNodes)
            level = nextLevel
        return ret[::-1]

node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(node1))
