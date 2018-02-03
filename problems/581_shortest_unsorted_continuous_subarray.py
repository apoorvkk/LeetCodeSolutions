'''
URL: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        start = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[start]:
                while start >= 0 and nums[i] < nums[start]:
                    start -= 1
                start += 1
                break
            start += 1

        if start == len(nums) - 1:
            return 0

        end = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[end]:
                while end < len(nums) and nums[i] > nums[end]:
                    end += 1
                end -= 1
                break
            end -= 1

        min_val, max_val = nums[start], nums[end]
        for i in range(start, end+1):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])

        u_start, u_end = -1, -1

        for i in range(start):
            if min_val < nums[i]:
                u_start = i
                break

        for j in range(len(nums)-1, end, -1):
            if max_val > nums[j]:
                u_end = j
                break

        if u_start == -1:
            u_start = start
        if u_end == -1:
            u_end = end

        return u_end - u_start + 1
