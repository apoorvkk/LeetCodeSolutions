# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        reversed_lst_start = None
        reversed_lst_end = None
        
        count = 1
        start = head
        end = head
        
        '''
        1->2
        
        count = 1
        '''
        while start is not None and end is not None:
            while count < k and end.next is not None:
                end = end.next
                count += 1
            
            if count < k:
                if reversed_lst_start:
                    reversed_lst_end.next = start
                else:
                    return head
                break

            next_node = end.next
            end.next = None
            self._reverse(start, end)
            
            if reversed_lst_start:
                reversed_lst_end.next = end
                reversed_lst_end = start
            else:
                reversed_lst_start = end
                reversed_lst_end = start
            

            # move to next multiple
            start = next_node
            end = start
            count = 1
            
        return reversed_lst_start
    
    def _reverse(self, start, end):
        reversed_node = start
        curr_node = reversed_node.next
        reversed_node.next = None
        
        next_node = None
        if curr_node:
            next_node = curr_node.next
        
        while curr_node is not None:
            curr_node.next = reversed_node
            reversed_node = curr_node
            curr_node = next_node
            
            if next_node:
                next_node = next_node.next
        
        