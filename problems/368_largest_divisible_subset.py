'''
URL: https://leetcode.com/problems/largest-divisible-subset/description/
Time complexity: O(n^2)
Space complexity: O(n)
'''

class Solution:

    def __init__(self):
        self.starting_val = None
        self.curr_max_subset_count = 0

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        subsets = {}
        for i in range(len(nums)):
            self.find_subsets(nums, i, subsets)

        curr_num = self.starting_val
        largest_subset = []
        while curr_num is not None:
            largest_subset.append(curr_num)
            curr_num = subsets[curr_num][0]
        return largest_subset

    def find_subsets(self, nums, index, subsets):
        if index >= len(nums):
            return None

        curr_num = nums[index]
        adj_num = None
        max_subset_count = 1

        for i in range(index+1, len(nums)):
            next_num = nums[i]

            if next_num % curr_num == 0:
                if next_num not in subsets:
                    self.find_subsets(nums, i, subsets)

                if subsets[next_num][1] + 1 > max_subset_count:
                    adj_num = next_num
                    max_subset_count = subsets[next_num][1] + 1

        subsets[curr_num] = (adj_num, max_subset_count)
        if max_subset_count > self.curr_max_subset_count:
            self.curr_max_subset_count = max_subset_count
            self.starting_val = curr_num
