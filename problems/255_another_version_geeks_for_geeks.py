'''

A solution for https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/

'''
class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) <= 1:
            return True
        root = Node(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            curr_val = preorder[i]
            curr_node = Node(curr_val)

            if curr_val <= stack[-1].val:
                stack[-1].left = curr_node
                stack.append(curr_node)
            else:
                while len(stack) > 0 and stack[-1].val < curr_val:
                    next_node = stack.pop()

                next_node.right = curr_node
                stack.append(curr_node)
        return root
