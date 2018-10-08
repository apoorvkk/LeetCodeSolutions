'''
URL: https://leetcode.com/problems/exclusive-time-of-functions
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Log:
    def __init__(self, func_id, end_type, timestamp):
        self.func_id = func_id
        self.is_start = True if end_type == "start" else False
        self.timestamp = timestamp

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        if len(logs) in (0,1):
            return []

        stack = []
        times_taken = defaultdict(int)
        for i in range(len(logs)):
            curr_log = self._decode_log(logs[i])

            if curr_log.is_start:
                stack.append([curr_log, 0])
            else:
                start_log = stack[-1][0]
                start_log_call_time = stack[-1][1]
                total_time = (curr_log.timestamp - start_log.timestamp + 1)
                times_taken[curr_log.func_id] += total_time - start_log_call_time
                stack.pop()

                if len(stack) > 0:
                    stack[-1][1] += total_time

        times = []
        for i in range(n):
            times.append(times_taken[i])
        return times


    def _decode_log(self, log):
        tokens = log.split(":")
        return Log(int(tokens[0]), tokens[1], int(tokens[2]))
