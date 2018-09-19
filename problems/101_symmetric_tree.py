'''
URL: https://leetcode.com/problems/symmetric-tree/description/
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, A):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if A is None:
            return True
        return self.aux_is_symmetric(A.left, A.right)

    def aux_is_symmetric(self, left, right):
        if not left and not right:
            return True

        if left and right and left.val == right.val:
            return self.aux_is_symmetric(left.left, right.right) and self.aux_is_symmetric(left.right, right.left)

        return False
