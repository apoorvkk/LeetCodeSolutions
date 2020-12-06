'''
URL: https://leetcode.com/problems/boundary-of-binary-tree/submissions/
Time complexity: O(n)
Space complexity: O(h)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        if not root.left and not root.right:
            return [root.val]

        ordered_nodes = [root.val]
        self.left_leaf = None

        if root.left:
            self._left_boundary(root.left, ordered_nodes)

        self._leaves(root, ordered_nodes)

        if root.right:
            self._right_boundary(root.right, ordered_nodes)

        return ordered_nodes

    def _left_boundary(self, node, nodes):
        nodes.append(node.val)

        if node.left:
            self._left_boundary(node.left, nodes)
        elif node.right:
            self._left_boundary(node.right, nodes)
        else: # left most leaf
            self.left_leaf = node

    def _right_boundary(self, node, nodes):
        if node.right:
            self._right_boundary(node.right, nodes)
        elif node.left:
            self._right_boundary(node.left, nodes)

        if node.right or node.left:
            nodes.append(node.val)

    def _leaves(self, node, nodes):
        if not node.left and not node.right and self.left_leaf != node:
            nodes.append(node.val)

        if node.left:
            self._leaves(node.left, nodes)
        if node.right:
            self._leaves(node.right, nodes)
