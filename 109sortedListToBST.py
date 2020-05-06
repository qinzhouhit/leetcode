'''
keys:the middle element of the given list would form the root of the binary search tree.
All the elements to the left of the middle element would form the left subtree recursively.
Similarly, all the elements to the right of the middle element will form the right subtree
of the binary search tree. This would ensure the height balance required in the resulting
 binary search tree.
Solutions:
Similar:
T:
S:
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TODO: method 3, inorder construction
    # T: O(N); S: O(logN), for the recursion stack,
    # bound by the height of the balanced BST
    def findSize(self, head):
        ptr = head
        ct = 0
        while ptr:
            ptr = ptr.next
            ct += 1
        return ct

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            # move to the next ListNode in linked list
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)

    # TODO: method 2, recursion + conversion to array
    # T: O(N): O(1) accessing for list; S: O(N) for the list
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        vals = self.mapListToValues(head)

        def convertListToBST(l, r):
            if l > r: # Invalid case
                return None
            mid = (l+r)//2
            node = TreeNode(vals[mid])

            if l == r:
                return node
            node.left = convertListToBST(l ,mid-1)
            node.right = convertListToBST(mid+1, r)
            return node
        return convertListToBST(0 ,len(vals)-1)


    # TODO: method 1, recursion
    # use two pointer to find out the middle element, slow and fast
    # slow is the middle when fast reaches the end
    def findMiddle(self, head):
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next # two steps

        # the case when slowPtr was equal to head, disconnect the left portion
        # otherwise, the findMiddle will loop the original linked list when we
        # wish to loop the left portion
        if prevPtr:
            prevPtr.next = None

        return slowPtr

    # S: O(logN), O(N) for a skewd tree, but O(logN) for balanced tree
    # T: O(NlogN), see solution
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        mid = self.findMiddle(head)
        node = TreeNode(mid.val) # The mid becomes the root of the BST.

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

lk1 = ListNode(-10)
lk2 = ListNode(-3)
lk3 = ListNode(0)
lk4 = ListNode(5)
lk5 = ListNode(9)
lk6 = ListNode(12)
lk1.next = lk2
lk2.next = lk3
lk3.next = lk4
lk4.next = lk5
lk5.next = lk6
sol = Solution()
print (sol.sortedListToBST1(lk1))
