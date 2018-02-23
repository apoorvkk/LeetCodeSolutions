'''
URL: https://leetcode.com/problems/is-subsequence/description/
Time complexity: O(n) with n proportionate to t
Space complexity: O(n) with n proportionate to t

Follow up (check follow up description in link):
Time complexity: O(m log k) with m being size of string s and k ranging from 0 to length of string t
Space complexity: O(1)
'''

from collections import defaultdict

class Solution:

    def __init__(self):
        self.t_lookup = defaultdict(list)

    def pre_process(self, t):
        for i, letter in enumerate(t):
            self.t_lookup[letter].append(i)

    def binary_search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            if target > nums[end]:
                if end+1 < len(nums):
                    return nums[end+1]
                return -1
            if target < nums[start]:
                return nums[start]

            mid = (start + end) // 2
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] > target:
                prev_mid_val = nums[mid]
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        return -1

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.pre_process(t)

        prev_index_in_subsequence = -1
        for curr_index, curr_letter in enumerate(s):
            if len(self.t_lookup[curr_letter]) == 0:
                return False

            next_index = -1
            if prev_index_in_subsequence == -1:
                next_index = self.t_lookup[curr_letter][0]
            else:
                next_index = self.binary_search(self.t_lookup[curr_letter], prev_index_in_subsequence)
            if next_index == -1:
                return False
            prev_index_in_subsequence = next_index + 1
        return True

