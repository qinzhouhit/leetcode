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
    # educative.io, O(N) for S and T
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            len_ = len(q)
            prev = None
            # we dont need to process last node of each level as 
            # cur.next = None since by default next is None
            for _ in range(len_):
                cur = q.popleft()
                if prev:
                    prev.next = cur
                prev = cur 

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return root

    # self-made， O(N) for S and T
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            l = len(q)
            for i in range(len(q)):
                node = q.popleft()
                # print (q, node.val)
                if i == l-1:
                    node.next = None
                elif i < l-1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root



    def connect(self, root: 'Node') -> 'Node':
        if not root: return []

        import collections
        queue = collections.deque([root])
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node:
                node.next = queue[0]
                if node.left: queue += [node.left]
                if node.right: queue += [node.right]
            elif queue: # pay attention!!!
                queue += [None]
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
