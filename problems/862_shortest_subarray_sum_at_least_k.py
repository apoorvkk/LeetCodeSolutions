'''
URL: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import deque

class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 0:
            return -1

        B = [0]
        curr_sum = 0
        for num in A:
            curr_sum += num
            B.append(curr_sum)

        queue = deque()
        res = float('inf')
        for i in range(len(A)+1):
            while len(queue) > 0 and B[i] - B[queue[0]] >= K:
                res = min(res, i - queue.popleft())

            while len(queue) > 0 and B[i] <= B[queue[-1]]:
                queue.pop()

            queue.append(i)

        if res == float('inf'):
            return -1
        return res

