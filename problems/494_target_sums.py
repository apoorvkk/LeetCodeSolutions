'''
URL: https://leetcode.com/problems/target-sum
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        return self._aux_find_target_combos(nums, S, {}, 0)

    def _aux_find_target_combos(self, nums, target, cache, i):
        if i == len(nums) - 1:
            if nums[i] == target or -nums[i] == target:
                if nums[i] == 0: return 2
                return 1
            return 0

        if (i, target) in cache:
            return cache[(i, target)]

        total_solns = 0
        total_solns += self._aux_find_target_combos(nums, target+nums[i], cache, i+1)
        total_solns += self._aux_find_target_combos(nums, target-nums[i], cache, i+1)

        cache[(i, target)] = total_solns
        return total_solns
