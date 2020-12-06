'''
URL: https://leetcode.com/problems/4sum
Time complexity: O(n^3)
Space complexity: O(n)
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.aux_n_sum(4, 0, len(nums)-1, nums, target, [], results)
        return results

    def aux_n_sum(self, N, start, end, nums, target, result, results):
        if N == 2:
            while start <= end-1:
                pot_target = nums[start] + nums[end]
                if pot_target == target:
                    results.append(result + [nums[start], nums[end]])
                    start += 1

                    while start <= end-1 and nums[start] == nums[start-1]:
                        start += 1

                    end -= 1
                    while start <= end-1 and nums[end] == nums[end+1]:
                        end -= 1

                    if start > end-1:
                        break
                elif pot_target > target:
                    end -= 1
                elif pot_target < target:
                    start += 1
        else:
            for i in range(start, (end+1) - (N-1)):
                if i == start or nums[i] != nums[i-1]:
                    self.aux_n_sum(N-1, i+1, end, nums, target-nums[i], result+[nums[i]], results)
