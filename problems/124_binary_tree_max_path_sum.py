'''
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        self.global_max_sum = -float('inf')
        self.aux_max_path_sum(root)
        return self.global_max_sum


    def aux_max_path_sum(self, node):
        if node is None:
            return 0

        left_max_with_root = self.aux_max_path_sum(node.left)
        right_max_with_root = self.aux_max_path_sum(node.right)

        max_path_with_root = max(node.val, node.val + left_max_with_root, node.val + right_max_with_root)

        self.global_max_sum = max(self.global_max_sum, max_path_with_root, node.val + left_max_with_root + right_max_with_root)
        return max_path_with_root

