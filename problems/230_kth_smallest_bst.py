'''
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Time complexity: O(k)
Space complexity: O(h)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _add_left_nodes(self, node, stack):
        while node.left:
            stack.append(node.left)
            node = node.left

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return -1

        stack = []

        stack.append(root)
        curr_node = root
        self._add_left_nodes(root, stack)

        while len(stack) > 0:
            curr_node = stack.pop()

            k -= 1

            if k == 0:
                return curr_node.val

            if curr_node.right:
                stack.append(curr_node.right)
                self._add_left_nodes(curr_node.right, stack)
        return -1
