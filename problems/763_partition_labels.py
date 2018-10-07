'''
URL: https://leetcode.com/problems/partition-labels
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 1:
            return 1

        letter_intervals = {}

        for i, char in enumerate(S):
            letter_intervals[char] = i

        parts = []
        start = 0
        end = 0
        for i in range(len(S)):
            curr_char = S[i]
            end = max(end, letter_intervals[curr_char])
            if i == end:
                parts.append(end - start + 1)
                start = end + 1

        return parts
