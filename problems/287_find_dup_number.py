'''
URL: https://leetcode.com/problems/find-the-duplicate-number/
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return -1

        lo, hi = 1, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                lo = mid + 1
            else: # count > mid
                hi = mid

        return lo
