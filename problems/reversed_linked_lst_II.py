# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m == n:
            return head
        
        # Find m (1 <= m < n <= length of list)
        b, curr_node = None, head
        for _ in range(m-1):
            b = curr_node
            curr_node = curr_node.next
            
        start_node = curr_node
        if b:
            b.next = None
        
        # Reverse list and find end node
        prev_node = curr_node
        curr_node = curr_node.next
        next_node = None
        if curr_node:
            next_node = curr_node.next
        
        n -= m
        for _ in range(n):
            curr_node.next = prev_node
            if prev_node.next == curr_node:
                prev_node.next = None
            
            prev_node = curr_node
            curr_node = next_node
            if next_node:
                next_node = next_node.next
            
        # connect start of reverse list to end node and end of reverse list to start node
        if b:
            b.next = prev_node
        start_node.next = curr_node
        
        if m > 1:
            return head
        return prev_node