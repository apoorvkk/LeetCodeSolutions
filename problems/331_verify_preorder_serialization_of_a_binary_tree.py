'''
URL: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
Time complexity: O(n)
Space complexity: O(height of tree)
'''

class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")

        if len(preorder) == 0:
            return True
        if self.validate_tree(preorder, 0) == len(preorder):
            return True
        return False

    def validate_tree(self, preorder, index):
        if index >= len(preorder):
            return index + 1
        curr_node = preorder[index]

        if not curr_node.isdigit():
            return index + 1

        # Left subtree
        next_index = self.validate_tree(preorder, index+1)

        # Right subtree
        next_index = self.validate_tree(preorder, next_index)

        return next_index
