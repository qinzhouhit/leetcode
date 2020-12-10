'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:
	# educative.io, O(N) for S and T
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        q = deque([root])
        while q:
            len_ = len(q)
            for i in range(len_):
                cur = q.popleft()
                if i == len_ - 1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res
        
    # official fancy ones
    # bfs two queues, one for cur level, one for nxt level
    def rightSideView1(self, root: TreeNode) -> List[int]:
        if root is None: return []
        
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)
        return rightside


    # bfs sentinel; use a sentinel node to separate the levels.
    def rightSideView2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root, None,])
        rightside = []
        
        curr = root
        while queue:
            prev, curr = curr, queue.popleft()
            while curr:
                # add child nodes in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                prev, curr = curr, queue.popleft()
            
            # the current level is finished
            # and prev is its rightmost element      
            rightside.append(prev.val)
            # add a sentinel to mark the end 
            # of the next level
            if queue:
                queue.append(None)
        
        return rightside

    # recursive DFS
    def rightSideView3(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        rightside = []
        
        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
                
        helper(root, 0)
        return rightside









        