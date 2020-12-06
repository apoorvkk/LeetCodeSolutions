'''
URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(inorder) != len(preorder):
            return None

        inorder_lookup = {}
        for i, val in enumerate(inorder):
            inorder_lookup[val] = i

        preorder_pointer = [0]
        return self.aux_construct_tree(preorder_pointer, preorder, inorder, 0, len(inorder)-1, inorder_lookup)


    def aux_construct_tree(self, preorder_pointer, preorder, inorder, start, end, inorder_lookup):
        if preorder_pointer[0] >= len(preorder) or start > end:
            return None

        curr_node = TreeNode(preorder[preorder_pointer[0]])
        curr_node_inorder_pos = inorder_lookup[curr_node.val]
        preorder_pointer[0] += 1

        curr_node.left = self.aux_construct_tree(preorder_pointer, preorder, inorder, start, curr_node_inorder_pos-1, inorder_lookup)
        curr_node.right = self.aux_construct_tree(preorder_pointer, preorder, inorder, curr_node_inorder_pos+1, end, inorder_lookup)

        return curr_node

