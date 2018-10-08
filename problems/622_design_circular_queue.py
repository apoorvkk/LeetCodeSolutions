# URL: https://leetcode.com/problems/design-circular-queue
class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None for i in range(k)]
        self.start = -1
        self.end = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.queue[0] = value
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % len(self.queue)
            self.queue[self.end] = value
        return True


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        old_start = self.start
        self.queue[self.start] = None
        self.start = (self.start + 1) % len(self.queue)

        if old_start == self.end: # There was only 1 elem to delete
            self.start = -1
            self.end = -1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.start]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.end]
        return -1


    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.start == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if abs(self.start - self.end) + 1 == len(self.queue):
            return True

        if self.start == self.end + 1:
            return True

        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
