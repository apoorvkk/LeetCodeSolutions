'''
URL: https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        sorted_lst = []
        self.sort_vals(root, sorted_lst)

        min_diff = -1
        for i in range(len(sorted_lst)-1):
            curr_diff = abs(sorted_lst[i] - sorted_lst[i+1])
            if min_diff == -1:
                min_diff = curr_diff
            else:
                min_diff = min(min_diff, curr_diff)


        return min_diff

    def sort_vals(self, node, sorted_lst):
        if node is None:
            return None

        self.sort_vals(node.left, sorted_lst)
        sorted_lst.append(node.val)
        self.sort_vals(node.right, sorted_lst)
