# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
        
        
          10
         /   \
        4     20
     /   \    /  \
    1     8  12   30
     \           /
      3         28

l = 2, r = 30

if node is smaller or equal to range:
    try to go right subtree if exists

if node is greater or equal to range:
    try to go left subtree if exists

if node in range:
    try both subtrees
    
'''


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.total = 0
        
        self._sum_tree(root, L, R)
        
        return self.total
    
    def _sum_tree(self, root, l, r):
        if root is None:
            return
        
        if l <= root.val <= r:
            self.total += root.val
        
        if l < root.val < r:
            self._sum_tree(root.left, l, r)
            self._sum_tree(root.right, l, r)
        elif root.val <= l:
            self._sum_tree(root.right, l, r)
        elif root.val >= r:
            self._sum_tree(root.left, l, r)