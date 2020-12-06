'''
URL: https://leetcode.com/problems/increasing-triplet-subsequence/
Time complexity: O(nl)
Space complexity: O(1)
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        min_vals_lengths = [None for i in range(4)]

        min_vals_lengths[1] = nums[0]
        longest_length = 1

        for i in range(1, len(nums)):
            curr_num = nums[i]

            for j in range(longest_length, -1, -1):

                if j == 0:
                    min_vals_lengths[j+1] = min(min_vals_lengths[j+1], curr_num)
                elif curr_num > min_vals_lengths[j]:
                    if min_vals_lengths[j+1] == None:
                        min_vals_lengths[j+1] = curr_num
                        longest_length += 1
                    else:
                        min_vals_lengths[j+1] = min(min_vals_lengths[j+1], curr_num)

                if longest_length == 3:
                    return True
        return False



