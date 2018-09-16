'''
URL: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
Time complexity: O(n)
Space complexity: O(1)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        small, big = self.aux_doubly_linked(root)

        big.right = small
        small.left = big

        return small


    def aux_doubly_linked(self, node):
        left_small = node
        right_big = left_small

        if node.left:
            left_small, left_big = self.aux_doubly_linked(node.left)
            node.left = left_big
            left_big.right = node

        if node.right:
            right_small, right_big = self.aux_doubly_linked(node.right)
            node.right = right_small
            right_small.left = node

        return left_small, right_big
