'''
URL: https://leetcode.com/problems/recover-binary-search-tree/
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

    def _inorder(self, node):
        if node is None:
            return

        self._inorder(node.left)

        if self.first_elem == None and self.prev_elem.val >= node.val:
            self.first_elem = self.prev_elem

        if self.first_elem != None and self.prev_elem.val >= node.val:
            self.second_elem = node
        self.prev_elem = node

        self._inorder(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None or (not root.left and not root.right):
            return
        self.first_elem = None
        self.second_elem = None
        self.prev_elem = TreeNode(-float('inf'))

        self._inorder(root)

        self.first_elem.val, self.second_elem.val = self.second_elem.val, self.first_elem.val
