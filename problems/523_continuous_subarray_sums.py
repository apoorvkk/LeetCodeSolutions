'''
URL: https://leetcode.com/problems/continuous-subarray-sum
Time complexity: O(n)
Space complexity: O(k)
'''

class Solution(object):
    def _is_continuous_zeros(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        return False

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return self._is_continuous_zeros(nums)
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = cum_sum_mod_k + n

            remainder = cum_sum_mod_k % k
            if remainder in mods and i - mods[remainder] > 1:
                return True
            if remainder not in mods:
                mods[remainder] = i
        return False
