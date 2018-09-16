'''
URL: https://leetcode.com/problems/3sum-smaller/description/
Time complexity: O(n^2)
Space complexity: O(1)
'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        [3,1,0,-2]

        [-2, 0, 1, 3]
        """
        num_solutions = 0
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1

            while l < r:
                potential_sum = nums[i] + nums[l] + nums[r]

                if potential_sum >= target:
                    r -= 1
                else:
                    num_solutions += r - l

                    l += 1
            i += 1

        return num_solutions
