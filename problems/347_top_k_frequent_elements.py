'''
URL: https://leetcode.com/problems/top-k-frequent-elements/description/
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        bucket_counts = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            bucket_counts[count].append(num)

        k_mst_freq_elems = []

        for count in range(len(bucket_counts)-1, -1, -1):
            bucket = bucket_counts[count]

            i = 0
            while i < len(bucket) and k > 0:
                k_mst_freq_elems.append(bucket[i])
                k -= 1
                i += 1

            if k == 0:
                break

        return k_mst_freq_elems



