'''
URL: https://leetcode.com/problems/convert-bst-to-greater-tree/description/
Time complexity: O(n)
Space complexity: O(height of tree)
'''

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert_bst(root, 0)
        return root

    def convert_bst(self, root, parent_greater_val):
        if root is None:
            return 0
        old_root_val = root.val

        right_total_val = self.convert_bst(root.right, parent_greater_val)

        root.val += parent_greater_val
        if root.right:
            root.val += right_total_val

        left_total_val = self.convert_bst(root.left, root.val)
        return old_root_val + left_total_val + right_total_val
