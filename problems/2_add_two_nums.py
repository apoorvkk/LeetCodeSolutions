'''
URL: https://leetcode.com/problems/add-two-numbers/
Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_length(self, node):
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2

        l1_length = self.get_length(l1)
        l2_length = self.get_length(l2)

        if l1_length < l2_length:
            shorter_node = l1
            longer_node = l2
        else:
            shorter_node = l2
            longer_node = l1

        final_answer = None
        curr_answer = None
        carry_over = 0
        while shorter_node is not None or longer_node is not None:
            column_sum = carry_over + longer_node.val
            longer_node = longer_node.next

            if shorter_node:
                column_sum += shorter_node.val
                shorter_node = shorter_node.next

            if final_answer:
                curr_answer.next = ListNode(column_sum % 10)
                curr_answer = curr_answer.next
            else:
                final_answer = ListNode(column_sum % 10)
                curr_answer = final_answer
            carry_over = 1 if column_sum >= 10 else 0

        if carry_over == 1:
            curr_answer.next = ListNode(1)
        return final_answer
