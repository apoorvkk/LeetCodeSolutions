'''
URL: https://leetcode.com/problems/flip-equivalent-binary-trees/
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
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        return self._is_flip_equal(root1, root2)
    
    def _is_flip_equal(self, node_one, node_two):
        if None in [node_one, node_two]:
            return [None, None] == [node_one, node_two]
        
        if node_one.val != node_two.val:
            return False
        
        if self._is_flip_equal(node_one.left, node_two.left) and self._is_flip_equal(node_one.right, node_two.right):
            return True
        return self._is_flip_equal(node_one.left, node_two.right) and self._is_flip_equal(node_one.right, node_two.left)
                