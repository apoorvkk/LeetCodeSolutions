'''
URL: https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) <= 1:
            return True

        j = -1
        min_val = -float("inf")
        for i in range(len(preorder)):
            curr_node = preorder[i]
            if curr_node <= min_val: # If true, there's a value in the right subtree that is smaller than the root in a bst.
                return False

            while j >= 0 and preorder[j] < curr_node:
                # Pop from our stack.
                min_val = preorder[j]
                j -= 1
            # Push to stack.
            j += 1
            preorder[j] = curr_node
        return True





