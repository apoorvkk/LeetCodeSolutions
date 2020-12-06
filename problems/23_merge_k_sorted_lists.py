'''
URL: https://leetcode.com/problems/merge-k-sorted-lists
Time complexity: O(nk logk) -> https://web.cs.dal.ca/~whidden/CS3110/assignments/a5_solution.pdf
Space complexity: O(log k)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self._merge_aux(lists, 0, len(lists)-1)

    def _merge_aux(self, lists, start, end):
        if start < end:
            mid = (start + end) // 2
            first_sorted_list = self._merge_aux(lists, start, mid)
            second_sorted_list = self._merge_aux(lists, mid+1, end)

            sorted_list = self._merge(first_sorted_list, second_sorted_list)
            return sorted_list
        elif start == end:
            return lists[start]
        else:
            return None

    def _merge(self, first_head, second_head):
        if not first_head and not second_head:
            return None

        sorted_head = None
        if not first_head and second_head:
            sorted_head = second_head
            second_head = second_head.next
        elif first_head and not second_head:
            sorted_head = first_head
            first_head = first_head.next
        elif first_head.val <= second_head.val:
            sorted_head = first_head
            first_head = first_head.next
        else:
            sorted_head = second_head
            second_head = second_head.next
        curr_node = sorted_head

        while first_head or second_head:
            if not first_head and second_head:
                curr_node.next = second_head
                second_head = second_head.next
            elif first_head and not second_head:
                curr_node.next = first_head
                first_head = first_head.next
            elif first_head.val <= second_head.val:
                curr_node.next = first_head
                first_head = first_head.next
            else:
                curr_node.next = second_head
                second_head = second_head.next
            curr_node = curr_node.next

        return sorted_head

