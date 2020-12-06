'''
URL: https://leetcode.com/problems/find-peak-element
Time complexity: O(logn)
Space complexity: O(1)
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            lower = max(0, mid-1)
            higher = min(len(nums)-1, mid+1)
            if nums[lower] < nums[mid] > nums[higher]:
                return mid
            elif mid == 0 and nums[mid] > nums[higher]:
                return mid
            elif mid == len(nums) - 1 and nums[mid] > nums[lower]:
                return mid
            elif nums[lower] < nums[mid] < nums[higher]:
                start = mid + 1
            elif nums[lower] > nums[mid] > nums[higher]:
                end = mid - 1
            else:
                start = mid + 1

        return 0
