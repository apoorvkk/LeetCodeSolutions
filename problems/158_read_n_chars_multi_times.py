'''
URL: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times
'''

from collections import deque

class Solution(object):
    def __init__(self):
        self.queue = deque()

    def read(self, buf, n):
        '''
        We are reading up to max n characters from a file.
        We need to put max n characters into the destination buf (buffer).
        This code essentially uses a queue to maintain the characters read from read4 and any overflow of characters (i.e n = 10, we call read4 3 times meaning the queue will have 2 characters left at the end of the function. These two characters will be used FIRST in the next read call).
        '''
        chars_read = 0

        while n > 0:
            buf4 = [""] * 4
            _ = read4(buf4)
            self.queue.extend(buf4)

            chars_to_read = min(len(self.queue), n)
            if chars_to_read == 0: # no more chars in the file or we have read enough chars
                return chars_read

            for i in range(chars_to_read):
                buf[chars_read] = self.queue.popleft()
                chars_read += 1
                n -= 1
        return chars_read
