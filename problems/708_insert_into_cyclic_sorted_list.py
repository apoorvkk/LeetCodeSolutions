'''
URL: https://leetcode.com/problems/insert-into-a-cyclic-sorted-list
Time complexity: O(n)
Space complexity: O(1)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        insert at the end:
            if bigger than curr_node or smaller than the next node
        """
        if head is None:
            return Node(insertVal, head)

        if head.next is None:
            curr_node = Node(insertVal, None)
            head.next = curr_node
            curr_node.next = head
            return head

        curr_node = head
        next_node = curr_node.next
        new_node = Node(insertVal, None)
        is_starting = True
        while curr_node != head or is_starting:
            if curr_node.val <= insertVal <= next_node.val:
                curr_node.next = new_node
                new_node.next = next_node
                return head
            elif curr_node.val > next_node.val:
                if insertVal >= curr_node.val or insertVal <= next_node.val:
                    curr_node.next = new_node
                    new_node.next = next_node
                    return head

            curr_node = next_node
            next_node = next_node.next
            is_starting = False

        curr_node.next = new_node
        new_node.next = next_node
        return head


