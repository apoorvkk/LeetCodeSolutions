'''
URL: https://leetcode.com/problems/random-pick-index/
Time complexity: O(n)
Space complexity: O(1)
'''

from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        total_occurrences = 0
        res = -1
        for i, elem in enumerate(self.nums):
            if elem == target:
                next_index = randint(0, total_occurrences)

                if next_index == 0:
                    res = i
                total_occurrences += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
