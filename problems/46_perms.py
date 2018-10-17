'''
URL: https://leetcode.com/problems/permutations
Time complexity: O(n^2 * n!)
Space complexity: O(n)
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        self.aux_find_perms(nums, [], results)
        return results

    def aux_find_perms(self, nums, result, results):
        if len(result) == len(nums):
            results.append(result)
        else:
            for i in range(len(nums)):
                if nums[i] != None:
                    next_num = nums[i]
                    nums[i] = None
                    self.aux_find_perms(nums, result+[next_num], results)
                    nums[i] = next_num
