'''
URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:
    def _preorder(self, root):
        if root is None:
            return "NN,"

        return str(root.val) + "," + self._preorder(root.left) + self._preorder(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        return self._preorder(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        queue = deque(nodes)

        return self._build_tree(queue)

    def _build_tree(self, queue):
        curr_val = queue.popleft()
        if curr_val == "NN" or curr_val == "":
            return None

        root_node = TreeNode(curr_val)
        root_node.left = self._build_tree(queue)
        root_node.right = self._build_tree(queue)

        return root_node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
