'''
URL: https://leetcode.com/problems/add-two-numbers-ii/
Time complexity: O(n)
Space complexity: O(n)
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

    def pad_zeros(self, node, length):
        curr_node = node
        while length > 0:
            new_head = ListNode(0)
            new_head.next = curr_node
            curr_node = new_head
            length -= 1
        return curr_node

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
            l1 = self.pad_zeros(l1, abs(l1_length - l2_length))
        else:
            l2 = self.pad_zeros(l2, abs(l1_length - l2_length))

        answer, carry_over = self.add_two_nums(l1, l2)

        if carry_over == 1:
            first_node = ListNode(1)
            first_node.next = answer
            return first_node
        return answer

    def add_two_nums(self, node_one, node_two):
        if node_one.next is None:
            column_sum = node_one.val + node_two.val
            carry_over = 1 if column_sum >= 10 else 0
            return ListNode(column_sum % 10), carry_over

        answer, carry_over = self.add_two_nums(node_one.next, node_two.next)

        column_sum = node_one.val + node_two.val + carry_over
        carry_over = 1 if column_sum >= 10 else 0
        column_node = ListNode(column_sum % 10)
        column_node.next = answer
        return column_node, carry_over



