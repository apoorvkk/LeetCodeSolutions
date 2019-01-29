class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other_interval):
        return self.end <= other_interval.start
    
    def __gt__(self, other_interval):
        return self.start >= other_interval.end
    
    def __eq__(self, other_interval):
        '''
            -------  # our interval
                ------ # other interval
            
            ------
          ----
          
          ------------
              ----
          
          -------
        ------------
        
        ------
        ----
        '''
        return not (self.__lt__(other_interval) or self.__gt__(other_interval))
        
            
class TreeNode:
    def __init__(self, interval):
        self.val = interval
        self.left = None
        self.right = None
        
class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        new_interval = Interval(start, end)
        
        if not self.root:
            self.root = TreeNode(new_interval)
            return True

        curr_node = self.root
        prev_node = None
        child_dir = ''
        
        while curr_node is not None:
            prev_node = curr_node

            if curr_node.val == new_interval: #overlap
                return False
            elif new_interval > curr_node.val:
                curr_node = curr_node.right
                child_dir = 'right'
            else:
                curr_node = curr_node.left
                child_dir = 'left'
        
        if child_dir == 'right':
            prev_node.right = TreeNode(new_interval)
        else:
            prev_node.left = TreeNode(new_interval)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)