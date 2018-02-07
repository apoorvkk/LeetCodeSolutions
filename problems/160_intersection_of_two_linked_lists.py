'''
URL: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = self.find_length(headA)
        len_b = self.find_length(headB)
        diff_num_nodes = abs(len_a-len_b)

        longer_lst, shorter_lst = headA, headB
        if len_b > len_a:
            longer_lst, shorter_lst = shorter_lst, longer_lst

        for i in range(diff_num_nodes):
            longer_lst = longer_lst.next

        while longer_lst is not None and shorter_lst is not None:
            if longer_lst.val == shorter_lst.val:
                return longer_lst

            shorter_lst = shorter_lst.next
            longer_lst = longer_lst.next

        return None


    def find_length(self, head):
        count = 0
        curr_node = head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next

        return count

