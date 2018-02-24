'''
URL: https://leetcode.com/problems/partition-equal-subset-sum/description/
Time complexity: O(nk) where is n is size of nums and k is target sum
Space complexity: O(k)
'''

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total_sum = 0
        for num in nums:
            total_sum += num

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        can_sum = [False for i in range(target_sum+1)]
        can_sum[0] = True

        for num in nums:
            visited = set()
            for i in range(len(can_sum)):
                next_num = i + num
                if can_sum[i] and next_num < len(can_sum) and i not in visited and not can_sum[next_num]:
                    can_sum[next_num] = True
                    visited.add(next_num)
        return can_sum[-1]
