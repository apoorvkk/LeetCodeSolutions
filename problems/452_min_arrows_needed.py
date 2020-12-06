'''
URL: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) in (0, 1):
            return len(points)

        points.sort(key=lambda x: x[1])
        total_arrows = 1
        curr_end = points[0][1]

        for i in range(1, len(points)):
            next_point = points[i]

            if next_point[0] > curr_end:
                curr_end = next_point[1]
                total_arrows += 1

        return total_arrows
