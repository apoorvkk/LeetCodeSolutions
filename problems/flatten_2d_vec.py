class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        
        [
          [1,2],
          [10],
          [4,5,6]
        ]
        """
        self.lists = vec2d
        self.curr_list = None
        self.curr_elem = None

    def next(self):
        """
        :rtype: int
        """
        if self.curr_list is not None and self.curr_list < len(self.lists):
            return self.lists[self.curr_list][self.curr_elem]
        return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self._inc_pointers()
        return self.curr_list < len(self.lists)
    
    def _inc_pointers(self):
        if self.curr_list is None:
            self._find_next_list(0)
            if self.curr_list is not None:
                self.curr_elem = 0
        else:
            if self.curr_elem < len(self.lists[self.curr_list]) - 1:
                self.curr_elem += 1
            else:
                self._find_next_list(self.curr_list + 1)
                if self.curr_list is not None:
                    self.curr_elem = 0
    
    def _find_next_list(self, index):
        while index < len(self.lists) and len(self.lists[index]) == 0:
            index += 1
        
        self.curr_list = index
    
    
    
'''
curr_list
    None -> has not been initialized
    valid index -> points to a list with elements
    invalid index -> finished
'''
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())