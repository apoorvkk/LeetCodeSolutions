'''
URL: https://leetcode.com/problems/sliding-window-maximum
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = deque()

        for i in range(len(nums)):

            while len(queue) > 0 and queue[0] < i - k + 1:
                queue.popleft()

            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res
