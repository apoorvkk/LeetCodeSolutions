class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        second_last, last, prev  = None, None, None
        max_sum = float('-inf')

        for i in range(len(nums)):
            curr = None

            if nums[i] > 0:
                l = float('-inf') if last is None else last
                sl = float('-inf') if second_last is None else second_last
                curr = nums[i] + max(l, sl, 0)
                max_sum = max(max_sum, curr)

            if prev is not None:
                second_last = last
                last = prev
            prev = curr

        if max_sum == float('-inf'): # all negs
            return max(nums)
        return max_sum