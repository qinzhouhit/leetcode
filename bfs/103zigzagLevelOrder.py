'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # educative.io version
    def zigzagLevelOrder5(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root: return result
        from collections import deque
        q = deque([root])
        flag = 1
        while q:
            lvl_size = len(q)
            lvl_vals = deque()

            for _ in range(lvl_size):
                node = q.popleft()
                if flag:
                    lvl_vals.append(node.val)
                else: # brilliant to use appendleft
                    lvl_vals.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag ^= 1
            result.append(list(lvl_vals))
        return result
        
    
    # based on LC 102
    def zigzagLevelOrder4(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        
        level = [(root, 0)]
        flag = 0
        while level:
            curNodes = []
            nextLevel = []
            for node in level:
                flag = node[1]
                curNodes.append(node[0].val)
                if node[0].left:
                    nextLevel.append((node[0].left, flag+1))
                if node[0].right:
                    nextLevel.append((node[0].right, flag+1))
            
            if not flag % 2: # even
                res.append(curNodes)
            else:
                res.append(curNodes[::-1])
            level = nextLevel

        return res
    
    # dfs, better than bfs
    def zigzagLevelOrder2(self, root):

        if root is None:
            return []

        def dfs(node, level):
            if level == len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else: # appendleft is smart
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        results = []
        dfs(root, 0)
        return results
    
    
    
    # bfs
    def zigzagLevelOrder3(self, root):

        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret

    
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        import collections
        if not root: return []
        queue, res = collections.deque([root]), []
        flag = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp+=[node.val]
                if node.left: queue+=[node.left]
                if node.right: queue+=[node.right]
            res += [tmp[::flag]]
            flag*=-1
        return res

node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.zigzagLevelOrder(node1))
