'''
URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 0 or len(inorder) != len(postorder):
            return None

        self.inorder_lookup = {}
        for i, val in enumerate(inorder):
            self.inorder_lookup[val] = i

        self.postorder_pointer = [len(postorder)-1]
        return self.aux_construct_tree(inorder, postorder, 0, len(inorder)-1)

    def aux_construct_tree(self, inorder, postorder, start, end):
        if start > end or self.postorder_pointer <= 0:
            return None

        curr_node = TreeNode(postorder[self.postorder_pointer[0]])
        curr_node_inorder_pos = self.inorder_lookup[curr_node.val]
        self.postorder_pointer[0] -= 1

        curr_node.right = self.aux_construct_tree(inorder, postorder, curr_node_inorder_pos+1, end)
        curr_node.left = self.aux_construct_tree(inorder, postorder, start, curr_node_inorder_pos-1)

        return curr_node

