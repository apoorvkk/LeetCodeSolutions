'''
URL: https://leetcode.com/problems/binary-tree-postorder-traversal
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        postorder = []
        stack = [(root, False)]

        while len(stack) > 0:
            curr_node, has_added_children = stack.pop()

            if not has_added_children:
                stack.append((curr_node, True))

                if curr_node.right:
                    stack.append((curr_node.right, False))
                if curr_node.left:
                    stack.append((curr_node.left, False))
            else:
                postorder.append(curr_node.val)

        return postorder
