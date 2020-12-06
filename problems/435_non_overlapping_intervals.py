'''
URL: https://leetcode.com/problems/non-overlapping-intervals/description/
Time complexity: O(nlogn)
Space complexity: O(1)
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.end)

        num_removals = 0
        end = intervals[0].end

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]

            if curr_interval.start >= end:
                end = curr_interval.end
            else:
                num_removals += 1

        return num_removals
