'''
URL: https://leetcode.com/problems/wiggle-sort/description/
Time complexity: O(nlogn)
Space complexity: O(logn)
'''


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums)-1)
        self.wiggle_sort(nums)

    def wiggle_sort(self, nums):
        for i in range(len(nums)):
            if i % 2 == 1:
                nums[i], nums[min(i+1, len(nums)-1)] = nums[min(i+1, len(nums)-1)], nums[i]

    def quick_sort(self, nums, start, end):
        if start < end:
            end_of_small_bag = start
            for i in range(start+1, end+1):
                if nums[i] <= nums[start]:
                    end_of_small_bag += 1
                    nums[end_of_small_bag], nums[i] = nums[i], nums[end_of_small_bag]
            nums[start], nums[end_of_small_bag] = nums[end_of_small_bag], nums[start]

            self.quick_sort(nums, start, end_of_small_bag-1)
            self.quick_sort(nums, end_of_small_bag+1, end)

