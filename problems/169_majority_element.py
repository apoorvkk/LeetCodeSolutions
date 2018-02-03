'''
URL: https://leetcode.com/problems/majority-element/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        majority_elem = nums[0]

        for i in range(1, len(nums)):
            if counter == 0:
                majority_elem = nums[i]

            if nums[i] == majority_elem:
                counter += 1
            else:
                counter -= 1

        return majority_elem

