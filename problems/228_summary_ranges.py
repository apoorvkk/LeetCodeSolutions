'''
URL: https://leetcode.com/problems/summary-ranges/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        ranges = []
        start = 0
        end = 0

        while end < len(nums):
            while end+1 < len(nums) and nums[end+1] - 1 == nums[end]:
                end += 1

            if start != end:
                ranges.append(str(nums[start]) + "->" + str(nums[end]))
            else:
                ranges.append(str(nums[start]))
            end += 1
            start = end

        return ranges
