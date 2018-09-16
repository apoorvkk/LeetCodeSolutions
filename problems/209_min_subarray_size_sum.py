'''
URL: https://leetcode.com/problems/minimum-size-subarray-sum/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0

        if len(nums) == 1:
            if nums[0] >= s:
                return 1
            return 0
        if sum(nums) == s: return len(nums)
        start = 0
        end = 1
        curr_sum = nums[0]
        min_length = 0 if curr_sum < s else 1

        while end < len(nums):
            if curr_sum < s:
                curr_sum += nums[end]
                end += 1
            else:
                if min_length == 0:
                    min_length = end - start
                else:
                    min_length = min(min_length, end - start)
                curr_sum -= nums[start]
                start += 1

        while curr_sum > s and start < len(nums):
            curr_sum -= nums[start]
            start += 1

            if curr_sum >= s:
                if min_length == 0:
                    min_length = end - start
                else:
                    min_length = min(min_length, end - start)

        return min_length
