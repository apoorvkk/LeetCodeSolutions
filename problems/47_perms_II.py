'''
URL: https://leetcode.com/problems/permutations-ii/
Time complexity: O(n*n!)
Space complexity: O(n)
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        results = []
        self.aux_permute(results, [], counts, len(nums))
        return results

    def aux_permute(self, results, result, counts, size):
        if len(result) == size:
            results.append(result)
        else:
            for digit, count in counts.iteritems():
                if counts[digit] > 0:
                    counts[digit] -= 1

                    self.aux_permute(results, result + [digit], counts, size)

                    counts[digit] += 1
