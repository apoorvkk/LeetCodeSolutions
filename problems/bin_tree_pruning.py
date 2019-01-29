# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        self._aux_prune_tree(root)
        return root
    
    def _aux_prune_tree(self, node):
        if node is None:
            return True
        
        left_is_zero = self._aux_prune_tree(node.left)
        right_is_zero = self._aux_prune_tree(node.right)
        
        if left_is_zero:
            node.left = None
        
        if right_is_zero:
            node.right = None
        
        return node.val == 0 and left_is_zero and right_is_zero