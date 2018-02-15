'''
URL: https://leetcode.com/problems/sort-characters-by-frequency/description/
Time complexity: O(n)
Space complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """


        counts = defaultdict(int)

        for letter in s:
            counts[letter] += 1

        bucket_counts = [[] for i in range(len(s)+1)]

        for letter, count in counts.items():
            bucket_counts[count].append(letter)

        sorted_freq_text = ""
        for count in range(len(bucket_counts)-1, -1, -1):
            bucket = bucket_counts[count]
            for letter in bucket:
                sorted_freq_text += letter * count

        return sorted_freq_text
