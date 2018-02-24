'''
URL: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
Time complexity: O(n!)
Space complexity: O(n)
'''

class Solution:
    def partition_subsets(self, nums, visited, curr_subset, subset_sums, target_sum, limit):
        if subset_sums[curr_subset] == target_sum:
            if curr_subset + 1 >= len(subset_sums):
                return True
            return self.partition_subsets(nums, visited, curr_subset+1, subset_sums, target_sum, len(nums)-1)

        for i in range(limit, -1, -1):
            curr_num = nums[i]
            if visited[i]: continue

            if subset_sums[curr_subset] + curr_num <= target_sum:
                visited[i] = True
                subset_sums[curr_subset] += curr_num
                nxt = self.partition_subsets(nums, visited, curr_subset, subset_sums, target_sum, i-1)
                visited[i] = False
                subset_sums[curr_subset] -= curr_num
                if nxt:
                    return True
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total_count = 0
        for num in nums:
            total_count += num

        if total_count % k > 0 or len(nums) < k:
            return False

        target_sum = total_count // k
        subset_sums = [0 for i in range(k)]
        visited = [False for i in range(len(nums))]
        subset_sums[0] += nums[0]
        visited[0] = True

        return self.partition_subsets(nums, visited, 0, subset_sums, target_sum, len(nums)-1)
