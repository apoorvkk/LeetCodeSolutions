'''
URL: https://leetcode.com/problems/zigzag-iterator
Time complexity: O(1)
Space complexity: O(r) where r is number of lists
'''

from collections import deque

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.queue = deque()
        if len(v1) > 0:
            self.queue.append((0, 0))
        if len(v2) > 0:
            self.queue.append((1, 0))


    def next(self):
        """
        :rtype: int
        """
        row_index, col_index = self.queue.popleft()

        if col_index+1 < len(self.lists[row_index]):
            self.queue.append((row_index, col_index+1))

        return self.lists[row_index][col_index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
