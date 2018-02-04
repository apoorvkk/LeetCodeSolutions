'''
URL: https://leetcode.com/problems/split-bst/description/
(Recursive version) Time complexity: O(log n)
(Recursive version) Space complexity: O(height of tree)
(Iterative version) Time complexity: O(log n)
(Iterative version) Space complexity: O(height of tree)
'''

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

        if root is None:
            return [None, None]

        if root.val == V:
            large = root.right
            root.right = None
            return [root, large]

        if root.val < V:
            small, large = self.splitBST(root.right, V)
            root.right = small
            return [root, large]

        if root.val >= V:
            small, large = self.splitBST(root.left, V)
            root.left = large
            return [small, root]



# Iterative version:

#         smaller = None
#         smaller_inject = None
#         larger = None
#         larger_inject = None

#         if root is None:
#             return [None, None]

#         curr_node = root
#         while curr_node is not None:
#             old_node = curr_node
#             if V < curr_node.val:  # add to larger
#                 if larger == None:
#                     larger = TreeNode(curr_node.val)
#                     larger.right = curr_node.right
#                     larger_inject = larger
#                 else:
#                     larger_inject.left = TreeNode(curr_node.val)
#                     larger_inject = larger_inject.left
#                     larger_inject.right = curr_node.right
#                 curr_node = curr_node.left


#             elif V >= curr_node.val: # add to smaller
#                 if smaller == None:
#                     smaller = TreeNode(curr_node.val)
#                     smaller.left = curr_node.left
#                     smaller_inject = smaller
#                 else:
#                     smaller_inject.right = TreeNode(curr_node.val)
#                     smaller_inject = smaller_inject.right
#                     smaller_inject.left = curr_node.left
#                 curr_node = curr_node.right

#         return [smaller, larger]
