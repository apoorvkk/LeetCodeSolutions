'''
URL: https://leetcode.com/problems/meeting-rooms/
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            curr_interval = intervals[i]
            next_interval = intervals[i+1]

            if next_interval.start < curr_interval.end:
                return False

        return True
