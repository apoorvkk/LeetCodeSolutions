'''
URL: https://leetcode.com/problems/copy-list-with-random-pointer/description/
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
         ---
        |   |
        0 -> 0 -> 0 -> 0
             |    |
              ----


        clone_lookup_tbl = {
            label: cloned_node
        }

        1. Copy the linked list but without the random pointers. Create a clone lookup table
        2. Iterate over the linked list keeping two pointers (one for each linked list). This is where we link up the random pointers.
        """
        if head is None: return None

        curr_node = head
        prev_curr_copy_node = None
        curr_copy_node = None
        head_copy_node = None
        cloned_nodes_lookup = {}

        # Copy linked list without random pointers
        while curr_node is not None:
            curr_copy_node = RandomListNode(curr_node.label)

            cloned_nodes_lookup[curr_node.label] = curr_copy_node
            if head_copy_node is None:
                head_copy_node = curr_copy_node # First cloned node

            if prev_curr_copy_node is not None:
                prev_curr_copy_node.next = curr_copy_node

            prev_curr_copy_node = curr_copy_node

            curr_node = curr_node.next

        # Copy random pointers
        curr_node = head
        curr_copy_node = head_copy_node

        while curr_node is not None and curr_copy_node is not None:
            if curr_node.random:
                curr_copy_node.random = cloned_nodes_lookup[curr_node.random.label]

            curr_node = curr_node.next
            curr_copy_node = curr_copy_node.next

        return head_copy_node
