'''
URL: https://leetcode.com/problems/insert-interval/description/
Time complexity: O(n)
Space complexity: O(n)
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]

        new_intervals = []

        i = 0
        # Skip smaller intervals
        while i < len(intervals) and intervals[i].end < newInterval.start:
            new_intervals.append(intervals[i])
            i += 1

        # We are at newInterval.start <= intervals[i].end. We want to merge the given interval with the new interval
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(
                min(newInterval.start, intervals[i].start),
                max(newInterval.end, intervals[i].end)
            )
            i += 1

        new_intervals.append(newInterval)

        while i < len(intervals):
            new_intervals.append(intervals[i])
            i +=1

        return new_intervals

