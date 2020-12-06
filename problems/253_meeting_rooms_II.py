'''
URL: https://leetcode.com/problems/meeting-rooms-ii
Time complexity: O(nlogn)
Space complexity: O(n)
'''

class RoomInterval(Interval):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __lt__(self, other_room_interval):
        if self.end < other_room_interval.end:
            return True
        return False

from heapq import heappush, heappop

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) in (0, 1):
            return len(intervals)

        min_rooms = []

        intervals.sort(key=lambda x:x.start)

        first_interval = RoomInterval(intervals[0].start, intervals[0].end)
        heappush(min_rooms, first_interval)

        for i in range(1, len(intervals)):
            curr_interval = RoomInterval(intervals[i].start, intervals[i].end)

            if curr_interval.start >= min_rooms[0].end:
                heappop(min_rooms)

            heappush(min_rooms, curr_interval)

        return len(min_rooms)

