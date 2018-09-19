'''
URL: https://leetcode.com/problems/maximum-product-subarray/description/
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        end_min, end_max, global_max = 0,0,0

        for i in range(len(nums)):
            curr_num = nums[i]

            if curr_num > 0:
                if end_max > 0:
                    end_max *= curr_num
                elif end_max == 0:
                    end_max = curr_num

                if end_min < 0:
                    end_min *= curr_num


            elif curr_num == 0:
                end_min = 0
                end_max = 0

            elif curr_num < 0:
                new_end_min = end_min
                new_end_max = end_max

                if end_min < 0:
                    new_end_min *= curr_num
                elif end_min == 0:
                    new_end_min = curr_num

                if end_max > 0:
                    new_end_max *= curr_num

                end_min = min([new_end_min, new_end_max, 0, curr_num])
                end_max = max([new_end_max, new_end_min, 0, curr_num])


            global_max = max(global_max, end_max)

        return global_max


