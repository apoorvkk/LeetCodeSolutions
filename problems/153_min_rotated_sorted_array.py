'''
URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
Time complexity: O(logn)
Space complexity: O(1)
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            if start == end:
                return nums[start]

            if end - start == 1:
                return min(nums[end], nums[start])

            mid = (start + end) // 2

            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid + 1
            else:
                if mid == 0:
                    return nums[0]

                if nums[mid] < nums[mid-1]:
                    return nums[mid]

                end = mid - 1
        return -1


