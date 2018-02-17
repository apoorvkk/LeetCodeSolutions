'''
URL: https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        counts = defaultdict(int)

        prev_num = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == prev_num:
                count += 1
            else:
                counts[prev_num] = count
                prev_num = nums[i]
                count = 1

        counts[prev_num] = count
        prev_sequences = defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                continue

            if prev_sequences[num] > 0:
                prev_sequences[num] -= 1
                prev_sequences[num+1] += 1
            elif counts[num+1] > 0 and counts[num+2] > 0:
                counts[num+1] -= 1
                counts[num+2] -= 1
                prev_sequences[num+3] += 1
            else:
                return False

            counts[num] -= 1

        return True

