'''
URL: https://leetcode.com/problems/path-sum-iii
Time complexity: O(n)
Space complexity: O(height of tree)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        return self.aux_find_path_sums(root, defaultdict(int), 0, target)

    def aux_find_path_sums(self, node, running_sums, curr_sum, target):
        curr_sum += node.val
        total_paths = running_sums[curr_sum - target]

        running_sums[curr_sum] += 1
        if curr_sum == target:
            total_paths += 1

        if node.left:
            total_paths += self.aux_find_path_sums(node.left, running_sums, curr_sum, target)

        if node.right:
            total_paths += self.aux_find_path_sums(node.right, running_sums, curr_sum, target)

        running_sums[curr_sum] -= 1

        return total_paths

