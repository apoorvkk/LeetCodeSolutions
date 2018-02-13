'''
URL: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def __init__(self):
        self.min = float("inf")
        self.pre = None

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.bst_min(root)
        return self.min

    def bst_min(self, node):
        if node is None:
            return

        if node.left:
            self.bst_min(node.left)

        if self.pre is not None:
            self.min = min(self.min, abs(node.val - self.pre))
        self.pre = node.val

        if node.right:
            self.bst_min(node.right)

