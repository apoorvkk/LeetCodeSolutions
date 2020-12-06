'''
URL: https://leetcode.com/problems/number-of-recent-calls/
Time complexity: O(logn)
Space complexity: O(n)
'''

class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.nums.append(t)

        target = t - 3000
        index = self._bin_search(target)

        return len(self.nums) - index

    def _bin_search(self, target):
        start = 0
        end = len(self.nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if self.nums[mid] == target:
                return mid
            elif self.nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
