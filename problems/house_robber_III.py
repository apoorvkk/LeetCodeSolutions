# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        dp[i] = max(root + dp[i+2], dp[i+1])
        """
        if root is None:
            return 0
        return max(self._max_rob_sum(root))
    
    def _max_rob_sum(self, curr_house):
        if curr_house.left is None and curr_house.right is None:
            return curr_house.val, 0 # with root, without root
        
        left_house_with_root, left_house_without_root = 0, 0
        right_house_with_root, right_house_without_root = 0, 0
        
        if curr_house.left:
            left_house_with_root, left_house_without_root = self._max_rob_sum(curr_house.left)
        
        if curr_house.right:
            right_house_with_root, right_house_without_root = self._max_rob_sum(curr_house.right)
            
        
        curr_house_with_root = curr_house.val + left_house_without_root + right_house_without_root
        curr_house_without_root = max(left_house_with_root, left_house_without_root) + max(right_house_without_root, right_house_with_root)
        
        return curr_house_with_root, curr_house_without_root