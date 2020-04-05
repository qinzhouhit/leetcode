'''
keys:
Solutions:
Similar:
T:
S:
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root: return []

        import collections
        queue = collections.deque([root])
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node:
                node.next = queue[0]
                if node.left: queue+=[node.left]
                if node.right: queue+=[node.right]
            elif queue: # pay attention!!!
                queue+=[None]
        return root




node1 = Node(1)
node2 = node1.left = Node(2)
node3 = node1.right = Node(3)
node2.left = Node(4)
node2.right = Node(5)
node3.left = Node(6)
node3.right = Node(7)

obj = Solution()
print(obj.connect(node1))
