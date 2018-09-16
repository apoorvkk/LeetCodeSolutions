'''
URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
Time complexity: O(nlogn)
Space complexity: O(1)
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if head is None:
            return None

        return self.aux_bst(head, None)

    def aux_bst(self, start, end):
        slow = start
        fast = start

        if start == end:
            return None

        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next

        curr_node = TreeNode(slow.val)

        curr_node.left = self.aux_bst(start, slow)
        curr_node.right = self.aux_bst(slow.next, end)
        return curr_node


