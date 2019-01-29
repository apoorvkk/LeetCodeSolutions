# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
'''
         0
        / \
      2    4
     /   /  \
    1   3    -1
   / \   \     \  
  5  1    6     8

'''
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        
        next_left_node = root
        
        while next_left_node:
            next_left_node = self._connect(next_left_node)
    
    def _connect(self, curr_node):
        head, prev_node = None, None

        while curr_node:
            if curr_node.left:
                if not head: 
                    head = curr_node.left
                
                if prev_node:
                    prev_node.next = curr_node.left
                    
                prev_node = curr_node.left
                
                                        
            if curr_node.right:
                if not head: 
                    head = curr_node.right
                
                if prev_node:
                    prev_node.next = curr_node.right
                
                prev_node = curr_node.right
                
            curr_node = curr_node.next
            
        return head