'''
URL: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
Time complexity: O(n)
Space complexity: O(height of stacked doubly linked ds)
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None or (head.next is None and head.child is None):
            return head

        self._aux_flatten(head)
        return head

    def _aux_flatten(self, head):
        curr_node = head
        next_node = curr_node.next
        final_node = curr_node

        while curr_node is not None:
            if curr_node.child:
                start_node, end_node = self._aux_flatten(curr_node.child)

                curr_node.child = None
                curr_node.next = start_node
                start_node.prev = curr_node
                end_node.next = next_node
                if next_node:
                    next_node.prev = end_node

                final_node = end_node

            curr_node = next_node
            if next_node:
                final_node = next_node
                next_node = next_node.next


        return head, final_node
