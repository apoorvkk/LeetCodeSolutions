'''
URL: https://leetcode.com/problems/continuous-subarray-sum
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sums = defaultdict(int)
        running_sums[0] = 1
        cumul_sum = 0
        total = 0
        for i in range(len(nums)):
            cumul_sum += nums[i]

            if (cumul_sum - k) in running_sums:
                total += running_sums[cumul_sum-k]
            running_sums[cumul_sum] += 1

        return total
