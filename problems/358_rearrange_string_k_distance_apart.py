'''
URL: https://leetcode.com/problems/rearrange-string-k-distance-apart
Time complexity: O(n) (would be O(nlogn) but heap has max size of 26 letters here :) )
Space complexity: O(1) (would be O(n) but we have max 26 unique letters :) )
'''

from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s

        heap = []

        unique_letters = set(s)
        counts = defaultdict(int)
        for letter in s:
            counts[letter] += 1

        for letter, count in counts.items():
            heappush(heap, (-count, letter))

        res = ""

        chars_left = len(s)
        while chars_left > 0 and len(heap) > 0:
            if k >= chars_left:
                if chars_left == len(unique_letters):
                    while len(heap) > 0:
                        _, letter = heappop(heap)
                        res += letter
                    return res
                return ""

            selected_items = []

            for i in range(k):
                if len(heap) == 0:
                    return ""

                item = heappop(heap)

                selected_items.append(item)
                letter = item[1]
                res += letter
                chars_left -= 1

            for item in selected_items:
                if item[0]+1 < 0:
                    heappush(heap, (item[0]+1, item[1]))
                else:
                    unique_letters.remove(item[1])
        return res
