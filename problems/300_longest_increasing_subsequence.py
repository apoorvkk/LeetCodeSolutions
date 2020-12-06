'''
URL: https://leetcode.com/problems/longest-increasing-subsequence
Time complexity: O(nlogn)
Space complexity: O(n)
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums.insert(0, None) # [None, 10,9,2,5,3,7,101,18]

        max_vals = [None for i in range(len(nums))]
        max_vals[1] = nums[1]
        global_max_length = 1

        for i in range(2, len(nums)):
            curr_num = nums[i]

            start = 1
            end = global_max_length
            found = False
            while start <= end and not found:
                mid = (start + end) // 2

                if max_vals[mid] < curr_num:
                    start = mid + 1
                elif max_vals[mid] > curr_num:
                    if max_vals[mid-1] == None or max_vals[mid-1] < curr_num:
                        max_vals[mid] = curr_num
                        found = True
                    else:
                        end = mid - 1
                else:
                    found = True

            if not found:
                global_max_length += 1
                max_vals[global_max_length] = curr_num

        return global_max_length


