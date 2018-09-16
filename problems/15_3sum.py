'''
URL: https://leetcode.com/problems/3sum/description/
Time complexity: O(n^2)
Space complexity: O(1)
'''
from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        solutions = []
        i = 0
        nums.sort()
        while i < len(nums) - 2:
            l = i+1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while l < r:
                potential_sum = nums[i] + nums[l] + nums[r]
                if potential_sum > 0:
                    r -= 1
                elif potential_sum < 0:
                    l += 1
                else:
                    solutions.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
            i += 1

        return solutions
