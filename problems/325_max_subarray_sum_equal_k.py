'''
URL: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        [1, -1, 5, -2, 3]


        [1, 0, 5, 3, 6]
        """

        sums = defaultdict(int)

        curr_sum = 0
        max_length = 0
        for i in range(len(nums)):
            curr_num = nums[i]

            curr_sum += curr_num

            if curr_sum == k:
                max_length = i + 1
            elif curr_sum - k in sums:
                max_length = max(max_length, i - sums[curr_sum - k])


            if curr_sum not in sums:
                sums[curr_sum] = i
        return max_length

