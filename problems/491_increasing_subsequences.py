'''
URL: https://leetcode.com/problems/increasing-subsequences
Time complexity: O(n!)
Space complexity: O(n)
'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return []

        results = []

        self.aux_find_inc_seqs(results, [], 0, nums)

        return results

    def aux_find_inc_seqs(self, results, result, start, nums):
        if len(result) >= 2:
            results.append(result)

        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue
            if len(result) == 0 or nums[i] >= result[-1]:
                self.aux_find_inc_seqs(results, result + [nums[i]], i+1, nums)
                used.add(nums[i])


