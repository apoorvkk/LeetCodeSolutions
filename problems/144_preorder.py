'''
URL: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
Time complexity: O(n)
Space complexity: O(h)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []

        preorder = []
        stack = [root]

        while len(stack) > 0:
            curr_node = stack.pop()
            preorder.append(curr_node.val)

            if curr_node.right:
                stack.append(curr_node.right)

            if curr_node.left:
                stack.append(curr_node.left)


        return preorder
