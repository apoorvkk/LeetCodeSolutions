# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or (root.left is None and root.right is None):
            return root
        
        return self._flip(root)[0]
    
    def _is_leaf(self, node):
        return node and node.left is None and node.right is None
    
    def _flip(self, root):
        left_temp, right_temp = root.left, root.right
        root.left, root.right = None, None
        
        is_left_leaf, is_right_leaf = self._is_leaf(left_temp), self._is_leaf(right_temp)
        
        if is_left_leaf and is_right_leaf:
            left_temp.left = right_temp
            left_temp.right = root
            return left_temp, left_temp.right
        
        elif not right_temp and is_left_leaf:
            left_temp.right = root
            return left_temp, left_temp.right
        
        elif not left_temp and is_right_leaf:
            right_temp.left = root
            return right_temp, None
        
        left_temp_flipped, flip_node = self._flip(left_temp)
        flip_node.right = root
        flip_node.left = right_temp
        
        return left_temp_flipped, flip_node.right
        
        