'''
keys:
Solutions:
Similar:
T:
S:
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def transform(node):
            if node:
                vals.append(str(node.val))
                transform(node.left)
                transform(node.right)
            else:
                vals.append("#")
        vals = []
        transform(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def transform():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = transform()
            node.right = transform()
            return node
        vals = iter(data.split())
        return transform()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
