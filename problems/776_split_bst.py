# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]


          4    4 ->
        /   \
      2      10  4 -> 10
     / \    / \
    1   3  5   16   5 -> 10
 /  \     / \
         n . 9

    smaller:

    smaller.right =  curr_node + curr_node.left


    larger:
    larger.left = curr_node + curr_node.right


         4
        /   \
      2      6
     / \    / \
    1   3  5   7
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
