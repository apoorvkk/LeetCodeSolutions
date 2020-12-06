'''
URL: https://leetcode.com/problems/min-stack
Time complexity: O(1)
Space complexity: O(n)
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif self.min_stack[-1] >= x:
                self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            item = self.stack.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.min_stack[-1]
        return -1



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
