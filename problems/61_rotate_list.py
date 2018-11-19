'''
URL: https://leetcode.com/problems/rotate-list/
Time complexity: O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _find_tail(self, head):
        if head is None:
            return None, 0
        
        curr_node = head
        count = 1
        while curr_node.next is not None:
            curr_node = curr_node.next
            count += 1
        
        return curr_node, count
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail, list_length = self._find_tail(head)
        
        if tail is None:
            return None
        
        k = k % list_length
        if k == 0:
            return head
        
        tail.next = head
        curr_node = head
        for i in range(list_length - k - 1):
            curr_node = curr_node.next
        
        new_head = curr_node.next
        curr_node.next = None
        
        return new_head if not None else curr_node
        