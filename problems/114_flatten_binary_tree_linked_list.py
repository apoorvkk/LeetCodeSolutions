'''
URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Time complexity: O(n)
Space complexity: O(height of tree)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        self.aux_flatten(root)

    def aux_flatten(self, node):
        start_node = node
        end_node = node

        right_temp = node.right
        left_temp = node.left

        node.right = None
        node.left = None

        if left_temp:
            start_left, end_left = self.aux_flatten(left_temp)

            start_node.right = start_left
            end_node = end_left

        if right_temp:
            start_right, end_right = self.aux_flatten(right_temp)

            end_node.right = start_right
            end_node = end_right

        return start_node, end_node
