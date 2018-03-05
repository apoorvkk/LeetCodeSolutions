'''
URL: https://leetcode.com/problems/escape-the-ghosts/description/
Time complexity: O(n)
Space complexity: O(1)
'''

import math
class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        min_ghost_dist = float("inf")

        for ghost in ghosts:
            min_ghost_dist = min(min_ghost_dist, abs(ghost[0]-target[0]) + abs(ghost[1]-target[1]))

        targ_dist = abs(target[0]) + abs(target[1])

        return targ_dist < min_ghost_dist

