'''
URL: https://leetcode.com/problems/reorder-list
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if head is None:
            return
        if head.next is None:
            return
        if head.next.next is None:
            return

        prev_slow = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        prev_slow.next = None

        smaller_head = head
        bigger_head = self.reverse_list(slow)


        self.interleave_lists(smaller_head, bigger_head)

    def interleave_lists(self, smaller_head, bigger_head):
        curr_smaller = smaller_head.next
        curr_bigger = bigger_head
        curr_nodes = [curr_smaller, curr_bigger]
        interleaved_node = smaller_head

        i = 1
        while curr_nodes[0] is not None or curr_nodes[1] is not None:
            j = i % 2
            if curr_nodes[j] is not None:
                interleaved_node.next = curr_nodes[j]
                interleaved_node = interleaved_node.next
                curr_nodes[j] = curr_nodes[j].next

            i += 1

    def reverse_list(self, head):
        reversed_head = head
        unreversed_head = reversed_head.next
        next_node = unreversed_head.next
        head.next = None

        while unreversed_head is not None:
            unreversed_head.next = reversed_head

            reversed_head = unreversed_head
            unreversed_head = next_node
            if next_node is not None:
                next_node = next_node.next
        return reversed_head
