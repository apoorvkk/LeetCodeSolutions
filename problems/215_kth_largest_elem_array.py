'''
URL: https://leetcode.com/problems/kth-largest-element-in-an-array
Time complexity: O(n) if list is randomly shuffled.
Space complexity: O(1)
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1
        k_pos = len(nums) - k

        while start <= end:
            pivot = nums[start]
            end_small_bag = start

            for j in range(start+1, end+1):
                if nums[j] <= pivot:
                    nums[j], nums[end_small_bag+1] = nums[end_small_bag+1], nums[j]
                    end_small_bag += 1

            nums[end_small_bag], nums[start] = nums[start], nums[end_small_bag]

            if end_small_bag == k_pos:
                return nums[end_small_bag]
            elif end_small_bag > k_pos:
                end = end_small_bag - 1
            elif end_small_bag < k_pos:
                start = end_small_bag + 1

        return -1


