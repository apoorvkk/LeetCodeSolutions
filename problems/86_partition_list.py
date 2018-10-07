'''
URL: https://leetcode.com/problems/partition-list/
Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        small = None
        big = None
        starting_small = None
        starting_big = None

        curr_node = head
        while curr_node != None:
            if curr_node.val < x:

                if small:
                    small.next = curr_node
                    small = small.next
                else:
                    starting_small = curr_node
                    small = starting_small
            else:
                if big:
                    big.next = curr_node
                    big = big.next
                else:
                    starting_big = curr_node
                    big = starting_big
            curr_node = curr_node.next

        if small:
            small.next = starting_big
        else:
            return starting_big
        if big:
            big.next = None
        return starting_small

